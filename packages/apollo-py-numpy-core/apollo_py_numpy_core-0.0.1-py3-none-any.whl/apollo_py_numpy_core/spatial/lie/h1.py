from typing import Union, List

from apollo_py_numpy_core.spatial.quaternions import UnitQuaternion, Quaternion
import numpy.typing as npt
import numpy as np


class LieGroupH1(UnitQuaternion):
    @classmethod
    def identity(cls) -> 'LieGroupH1':
        return cls([1, 0, 0, 0])

    def ln(self) -> 'LieAlgH1':
        w, x, y, z = self
        acos = np.acos(w)
        if acos == 0.0:
            return LieAlgH1([0, 0, 0, 0])
        else:
            ss = acos / np.sin(acos)
            return LieAlgH1([0, ss * x, ss * y, ss * z])

    def __repr__(self) -> str:
        return f"LieGroupH1(\n{np.array2string(self)}\n)"

    def __str__(self) -> str:
        return f"LieGroupH1(\n{np.array2string(self)}\n)"


class LieAlgH1(Quaternion):
    def __new__(cls, wxyz: Union[List[float], npt.NDArray[np.float64]]) -> 'LieAlgH1':
        return super().__new__(cls, wxyz).view(cls)

    @classmethod
    def from_euclidean_space_element(cls, e: Union[List[float], npt.NDArray[np.float64]]) -> 'LieAlgH1':
        if isinstance(e, list):
            if len(e) != 3:
                raise ValueError("List must contain exactly three numbers.")
            e = np.array(e, dtype=np.float64)
        elif isinstance(e, np.ndarray):
            if e.shape != (3,):
                raise ValueError("Array must have shape (3,).")
        else:
            raise TypeError("Input must be either a list of three numbers or a numpy array with shape (3,).")
        return cls([0, e[0], e[1], e[2]])

    def exp(self) -> 'LieGroupH1':
        v = self[1:]
        vn = np.linalg.norm(v)
        if vn == 0.0:
            return LieGroupH1.identity()
        else:
            cc = np.cos(vn)
            ss = np.sin(vn) / vn
            return LieGroupH1.new_unchecked([cc, ss * v[0], ss * v[1], ss * v[2]])

    def vee(self) -> npt.NDArray[np.float64]:
        w, x, y, z = self
        return np.array([x, y, z])

    def __repr__(self) -> str:
        return f"LieAlgH1(\n{np.array2string(self)}\n)"

    def __str__(self) -> str:
        return f"LieAlgH1(\n{np.array2string(self)}\n)"
