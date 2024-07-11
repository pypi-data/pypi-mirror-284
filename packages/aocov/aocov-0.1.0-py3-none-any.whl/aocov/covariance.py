import torch
import scipy.special as sp
from pydantic import BaseModel, ConfigDict
import numpy as np
import aotools
import time


class VonKarman(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    device: str = "cpu"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        b1 = (2**(-5/6)) * sp.gamma(11/6) / (torch.pi**(8./3))
        b2 = ((24. / 5) * sp.gamma(6. / 5)) ** (5. / 6)
        self._vk_coeff = b1*b2
        # try to put an array on the device to make sure it's valid
        torch.zeros([1],device=self.device)

    def _bessel_kv(self, alpha: float, x: torch.Tensor):
        """As of July 2024, pytorch does not implement the modified bessel
        function of the second kind with arbitrary real order, e.g.,
        scipy.special.kv(), so we do a very annoying numpy conversion
        before going back to pytorch.
        Once there is a pytorch.special.bessel_kv() or equivalent, then we can
        stay in pytorch completely - especially important for GPU parallelism.
        """
        y = torch.zeros_like(x)
        y += torch.tensor(
            sp.kv(alpha, x.detach().cpu().numpy()), 
            device=self.device
        )
        return y

    def _vk_cov(self, x: torch.Tensor, *, r0: float, L0: float):
        cov = torch.zeros_like(x)
        x = x + 1e-15
        a = (L0/r0)**(5/3)
        xn = 2*torch.pi*x/L0
        c = xn**(5/6) * self._bessel_kv(5/6, xn)
        cov += a*self._vk_coeff*c
        return cov

    def vk_cov(self, x: np.ndarray, *, r0: float, L0: float):
        return self._vk_cov(
            torch.tensor(x, device=self.device),
            r0=r0,
            L0=L0
        ).detach().cpu().numpy()

class _DistancesGeneric(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    device: str = "cpu"
    _udistance: torch.Tensor = None
    _uindices: torch.Tensor = None
    _distance: torch.Tensor = None

    @property
    def sparsity(self):
        elements_used = self._udistance.shape[0]
        full_elements_used = self._distance.ravel().shape[0]
        return elements_used / full_elements_used

    def eval(self, function):
        """takes a function, and returns an array of the function evaluated
        element-wise for the distances in this object. The function should
        expect a numpy array to be evaluated element-wise.
        Note, if `function` expects a tensor, then try `_eval()` instead."""
        values = function(self._udistance.detach().cpu().numpy())
        output = values[self._uindices.detach().cpu().numpy()]
        return output

    def _eval(self, function):
        """takes a function, and returns an array of the function evaluated
        element-wise for the distances in this object. The function should
        expect a numpy array to be evaluated element-wise.
        Note, if `function` expects a np.ndarray, then try `eval()` instead."""
        values = function(self._udistance)
        output = values[self._uindices]
        return output


class DistancesXYXY(_DistancesGeneric):
    _x_in: torch.Tensor
    _y_in: torch.Tensor
    _x_out: torch.Tensor
    _y_out: torch.Tensor

    def __init__(self, x_out, y_out, x_in, y_in, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._x_in = torch.tensor(x_in, device=self.device)
        self._y_in = torch.tensor(y_in, device=self.device)
        self._x_out = torch.tensor(x_out, device=self.device)
        self._y_out = torch.tensor(y_out, device=self.device)
        self._distance = ((self._x_out[:, None] - self._x_in[None, :])**2 +
                          (self._y_out[:, None] - self._y_in[None, :])**2)**0.5
        self._udistance, self._uindices = torch.unique(
            self._distance,
            return_inverse=True
        )

class DistancesRR(_DistancesGeneric):
    _x_in: torch.Tensor
    _y_in: torch.Tensor
    _x_out: torch.Tensor
    _y_out: torch.Tensor

    def __init__(self, rr, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._distance = torch.tensor(rr, device=self.device)
        self._udistance, self._uindices = torch.unique(
            self._distance,
            return_inverse=True
        )


def phase_covariance(rr: np.ndarray, r0: float, 
                     L0: float, device: str = "cpu"):
    dist = DistancesRR(rr, device=device)
    vkcov = VonKarman(device=device)
    if device == "cpu":
        return dist.eval(lambda x : vkcov.vk_cov(x, r0=r0, L0=L0))
    else:
        return dist._eval(lambda x : vkcov._vk_cov(x, r0=r0, L0=L0))


def phase_covariance_xyxy(
        x_out: np.ndarray, y_out: np.ndarray, 
        x_in: np.ndarray, y_in: np.ndarray, 
        r0: float, L0: float, device: str = "cpu"):
    dist = DistancesXYXY(
        x_out=x_out, y_out=y_out,
        x_in=x_in, y_in=y_in,
        device=device)
    vkcov = VonKarman(device=device)
    if device == "cpu":
        return dist.eval(lambda x : vkcov.vk_cov(x, r0=r0, L0=L0))
    else:
        return dist._eval(lambda x : vkcov._vk_cov(x, r0=r0, L0=L0))


def test_vk_cov(device="cpu"):
    x = np.array([0.1, 1.1, 10.5])
    r0 = 0.1
    L0 = 25.0
    cov = VonKarman(device=device)
    y = cov.vk_cov(x, r0=r0, L0=L0)
    y0 = aotools.phase_covariance(x, r0=0.10, L0=25.0)
    assert np.allclose(y, y0)


def speed_comparison(n=1000, device="cpu"):
    x = np.random.random(n)
    r0 = 0.1
    L0 = 25.0
    cov = VonKarman(device=device)
    t1 = time.time()
    y = cov.vk_cov(x, r0=r0, L0=L0)
    t2 = time.time()
    y0 = aotools.phase_covariance(x, r0=r0, L0=L0)
    t3 = time.time()
    print("Coviance only comparison")
    print(f"aotools took {t3-t2:10.3e} sec")
    print(f"aocov   took {t2-t1:10.3e} sec")
    assert np.allclose(y, y0)


def test_distance_uniqueness(device="cpu"):
    x_in, y_in = np.meshgrid(np.arange(2), np.arange(2), indexing="xy")
    x_in = x_in.flatten()
    y_in = y_in.flatten()
    x_out, y_out = np.meshgrid(np.arange(2), np.arange(2), indexing="xy")
    x_out = x_out.flatten()
    y_out = y_out.flatten()
    distances = DistancesXYXY(x_in, y_in, x_out, y_out, device=device)
    assert distances.sparsity == 0.1875


def speed_comparison_distances_self(n=40, device="cpu"):
    cov = VonKarman(device=device)
    r0 = 0.1
    L0 = 25.0

    xx, yy = np.meshgrid(np.arange(n), np.arange(n), indexing="xy")
    xx = xx.flatten()
    yy = yy.flatten()

    t1 = time.time()

    # use Distance object and VonKarman object
    distances = DistancesXYXY(xx, yy, xx, yy, device=device)
    out = distances.eval(lambda x: cov.vk_cov(x, r0=r0, L0=L0))
    t2 = time.time()

    # use full distance matrix and aotools cov
    rr = ((xx[:, None]-xx[None, :])**2 + (yy[:, None]-yy[None, :])**2)**0.5
    aotools.phase_covariance(rr, r0=r0, L0=L0)
    t3 = time.time()

    print("self-distance matrix covariance comparison")
    print(f"aotools took {t3-t2:10.3e} sec")
    print(f"aocov   took {t2-t1:10.3e} sec")
    return out


def speed_comparison_distances_other(n=40, device="cpu"):
    cov = VonKarman(device=device)
    r0 = 0.1
    L0 = 25.0

    xx, yy = np.meshgrid(np.arange(n), np.arange(n), indexing="xy")
    xx = xx.flatten()
    yy = yy.flatten()

    t1 = time.time()

    # use Distance object and VonKarman object
    distances = DistancesXYXY(xx, yy, xx+np.pi, yy+np.exp(1), device=device)
    out = distances.eval(lambda x: cov.vk_cov(x, r0=r0, L0=L0))
    t2 = time.time()

    # use full distance matrix and aotools cov
    rr = ((xx[:, None]-xx[None, :])**2 + (yy[:, None]-yy[None, :])**2)**0.5
    aotools.phase_covariance(rr, r0=r0, L0=L0)
    t3 = time.time()

    print("other-distance matrix covariance comparison")
    print(f"aotools took {t3-t2:10.3e} sec")
    print(f"aocov   took {t2-t1:10.3e} sec")
    return out


if __name__ == "__main__":
    test_vk_cov()
    speed_comparison(n=1_000_000)
    test_distance_uniqueness()
    speed_comparison_distances_self(n=64)
    speed_comparison_distances_other(n=64)
