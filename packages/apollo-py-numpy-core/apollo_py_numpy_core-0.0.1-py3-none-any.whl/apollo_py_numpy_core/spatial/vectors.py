from typing import Union, List
import numpy as np


class V3(np.ndarray):
    def __new__(cls, xyz: Union[List[float], np.ndarray]) -> 'V3':
        obj = np.asarray(xyz, dtype=np.float64).view(cls)
        if obj.shape != (3,):
            raise ValueError("V3 must be a 3-vector.")
        return obj

    def to_lie_alg_so3(self) -> 'LieAlgSO3':
        from apollo_py_numpy_core.spatial.lie.so3 import LieAlgSO3
        return LieAlgSO3.from_euclidean_space_element(self)

    def to_lie_alg_h1(self) -> 'LieAlgH1':
        from apollo_py_numpy_core.spatial.lie.h1 import LieAlgH1
        return LieAlgH1.from_euclidean_space_element(self)

    def __repr__(self) -> str:
        return f"V3(\n{np.array2string(self)}\n)"

    def __str__(self) -> str:
        return f"V3(\n{np.array2string(self)}\n)"


class V6(np.ndarray):
    def __new__(cls, xyz: Union[List[float], np.ndarray]) -> 'V6':
        obj = np.asarray(xyz, dtype=np.float64).view(cls)
        if obj.shape != (6,):
            raise ValueError("V6 must be a 6-vector.")
        return obj

    def __repr__(self) -> str:
        return f"V6(\n{np.array2string(self)}\n)"

    def __str__(self) -> str:
        return f"V6(\n{np.array2string(self)}\n)"
