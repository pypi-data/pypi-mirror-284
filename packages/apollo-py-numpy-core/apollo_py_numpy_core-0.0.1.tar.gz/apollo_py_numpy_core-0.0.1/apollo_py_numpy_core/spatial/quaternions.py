from typing import Union, List, Any
import numpy.typing as npt
import numpy as np
from apollo_py_numpy_core.spatial.vectors import V3


class Quaternion(np.ndarray):
    def __new__(cls, wxyz: Union[List[float], np.ndarray]) -> 'Quaternion':
        obj = np.asarray(wxyz, dtype=np.float64).view(cls)
        if obj.shape != (4,):
            raise ValueError("Quaternion must be a 4-vector.")
        return obj

    def w(self):
        return self[0]

    def x(self):
        return self[1]

    def y(self):
        return self[2]

    def z(self):
        return self[3]

    def conjugate(self) -> 'Quaternion':
        w, x, y, z = self
        return Quaternion([w, -x, -y, -z])

    def inverse(self) -> 'Quaternion':
        conjugate = self.conjugate()
        norm_sq = np.linalg.norm(self) ** 2
        return Quaternion(conjugate / norm_sq)

    def __mul__(self, other: 'Quaternion') -> 'Quaternion':
        w1, x1, y1, z1 = self
        w2, x2, y2, z2 = other

        w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
        x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
        y = w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2
        z = w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2

        return Quaternion([w, x, y, z])

    def __matmul__(self, other: 'Quaternion') -> 'Quaternion':
        return self * other

    def __repr__(self) -> str:
        return f"Quaternion(\n{np.array2string(self)}\n)"

    def __str__(self) -> str:
        return f"Quaternion(\n{np.array2string(self)}\n)"


class UnitQuaternion(Quaternion):
    def __new__(cls, wxyz: Union[List[float], npt.NDArray[np.float64]]) -> 'UnitQuaternion':
        out = super().__new__(cls, wxyz)
        if not np.isclose(np.linalg.norm(out), 1.0, rtol=1e-7, atol=1e-7):
            raise ValueError("Unit quaternion must be unit length.")
        return out.view(cls)

    @classmethod
    def new_unchecked(cls, wxyz: Union[List[float], npt.NDArray[np.float64]]) -> 'UnitQuaternion':
        out = super().__new__(cls, wxyz)
        return out.view(cls)

    @classmethod
    def new_normalize(cls, wxyz: Union[List[float], npt.NDArray[np.float64]]) -> 'UnitQuaternion':
        out = super().__new__(cls, wxyz)
        n = out / np.linalg.norm(out)
        return cls(n)

    @classmethod
    def from_euler_angles(cls, xyz: Union[List[float], npt.NDArray[np.float64]]) -> 'UnitQuaternion':
        if isinstance(xyz, list):
            if len(xyz) != 3:
                raise ValueError("List must contain exactly three numbers.")
        elif isinstance(xyz, np.ndarray):
            if xyz.shape != (3,):
                raise ValueError("Array must contain exactly three numbers.")
        else:
            raise TypeError("Input must be either a list of three numbers or a numpy array of three numbers.")

        cy = np.cos(xyz[2] * 0.5)
        sy = np.sin(xyz[2] * 0.5)
        cp = np.cos(xyz[1] * 0.5)
        sp = np.sin(xyz[1] * 0.5)
        cr = np.cos(xyz[0] * 0.5)
        sr = np.sin(xyz[0] * 0.5)

        w = cr * cp * cy + sr * sp * sy
        x = sr * cp * cy - cr * sp * sy
        y = cr * sp * cy + sr * cp * sy
        z = cr * cp * sy - sr * sp * cy

        return cls([w, x, y, z])

    def inverse(self) -> 'UnitQuaternion':
        return self.conjugate()

    def to_rotation_matrix(self) -> 'Rotation3B':
        from apollo_py_numpy.spatial.rotation_matrices import Rotation3
        w, x, y, z = self
        matrix = [
            [1 - 2 * (y ** 2 + z ** 2), 2 * (x * y - z * w), 2 * (x * z + y * w)],
            [2 * (x * y + z * w), 1 - 2 * (x ** 2 + z ** 2), 2 * (y * z - x * w)],
            [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x ** 2 + y ** 2)]
        ]
        return Rotation3.new_unchecked(matrix)

    def map_point(self, v: V3) -> 'V3':
        qv = Quaternion([0.0, v[0], v[1], v[2]])
        res = self@qv@self.conjugate()
        return V3([res[1], res[2], res[3]])

    def __mul__(self, other: 'UnitQuaternion') -> 'UnitQuaternion':
        return UnitQuaternion.new_unchecked(super().__mul__(other))

    def __matmul__(self, other: 'UnitQuaternion') -> 'UnitQuaternion':
        return self * other

    def __repr__(self) -> str:
        return f"UnitQuaternion(\n{np.array2string(self)}\n)"

    def __str__(self) -> str:
        return f"UnitQuaternion(\n{np.array2string(self)}\n)"
