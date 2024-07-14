import numpy as np
from typing import Union, List
import numpy.typing as npt

from apollo_py_numpy_core.spatial.matrices import M3
from apollo_py_numpy_core.spatial.quaternions import UnitQuaternion
from apollo_py_numpy_core.spatial.vectors import V3


class Rotation3(M3):
    def __new__(cls, input_array: Union[List[List[float]], np.ndarray]) -> 'Rotation3':
        out = super().__new__(cls, input_array)
        if not np.allclose(out @ out.T, np.eye(3), rtol=1e-7, atol=1e-7):
            raise ValueError("Rotation matrix must be orthonormal.")

        return out.view(cls)

    @classmethod
    def new_unchecked(cls, input_array: Union[List[List[float]], np.ndarray]) -> 'Rotation3':
        out = super().__new__(cls, input_array)
        return out.view(cls)

    @classmethod
    def new_normalize(cls, input_array: Union[List[List[float]], npt.NDArray[np.float64]]) -> 'Rotation3':
        out = super().__new__(cls, input_array)

        u, _, vh = np.linalg.svd(out)
        rotation_matrix = np.dot(u, vh)

        if np.linalg.det(rotation_matrix) < 0:
            u[:, -1] *= -1
            rotation_matrix = np.dot(u, vh)

        return cls.new_unchecked(rotation_matrix)

    @classmethod
    def from_euler_angles(cls, xyz: Union[List[float], npt.NDArray[np.float64]]) -> 'Rotation3':
        if isinstance(xyz, list):
            if len(xyz) != 3:
                raise ValueError("List must contain exactly three numbers.")
        elif isinstance(xyz, np.ndarray):
            if xyz.shape != (3,):
                raise ValueError("Array must contain exactly three numbers.")
        else:
            raise TypeError("Input must be either a list of three numbers or a numpy array of three numbers.")

        roll, pitch, yaw = xyz

        R_x = np.array([
            [1, 0, 0],
            [0, np.cos(roll), -np.sin(roll)],
            [0, np.sin(roll), np.cos(roll)]
        ])

        R_y = np.array([
            [np.cos(pitch), 0, np.sin(pitch)],
            [0, 1, 0],
            [-np.sin(pitch), 0, np.cos(pitch)]
        ])

        R_z = np.array([
            [np.cos(yaw), -np.sin(yaw), 0],
            [np.sin(yaw), np.cos(yaw), 0],
            [0, 0, 1]
        ])

        rotation_matrix = R_z @ R_y @ R_x

        return cls(rotation_matrix)

    def inverse(self) -> 'Rotation3':
        return self.transpose()

    def to_unit_quaternion(self) -> 'UnitQuaternion':
        from apollo_py_numpy.spatial.quaternions import UnitQuaternion
        m = self
        trace = np.trace(m)
        if trace > 0:
            s = 0.5 / np.sqrt(trace + 1.0)
            w = 0.25 / s
            x = (m[2, 1] - m[1, 2]) * s
            y = (m[0, 2] - m[2, 0]) * s
            z = (m[1, 0] - m[0, 1]) * s
        elif (m[0, 0] > m[1, 1]) and (m[0, 0] > m[2, 2]):
            s = 2.0 * np.sqrt(1.0 + m[0, 0] - m[1, 1] - m[2, 2])
            w = (m[2, 1] - m[1, 2]) / s
            x = 0.25 * s
            y = (m[0, 1] + m[1, 0]) / s
            z = (m[0, 2] + m[2, 0]) / s
        elif m[1, 1] > m[2, 2]:
            s = 2.0 * np.sqrt(1.0 + m[1, 1] - m[0, 0] - m[2, 2])
            w = (m[0, 2] - m[2, 0]) / s
            x = (m[0, 1] + m[1, 0]) / s
            y = 0.25 * s
            z = (m[1, 2] + m[2, 1]) / s
        else:
            s = 2.0 * np.sqrt(1.0 + m[2, 2] - m[0, 0] - m[1, 1])
            w = (m[1, 0] - m[0, 1]) / s
            x = (m[0, 2] + m[2, 0]) / s
            y = (m[1, 2] + m[2, 1]) / s
            z = 0.25 * s

        return UnitQuaternion.new_unchecked([w, x, y, z])

    def map_point(self, v: V3) -> 'V3':
        return (self@v).view(V3)

    def __repr__(self) -> str:
        return f"Rotation3(\n{np.array2string(self)}\n)"

    def __str__(self) -> str:
        return f"Rotation3(\n{np.array2string(self)}\n)"




