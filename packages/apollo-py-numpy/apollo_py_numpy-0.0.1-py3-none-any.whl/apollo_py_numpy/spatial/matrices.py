import numpy as np
from typing import Union, List


class M3(np.ndarray):
    def __new__(cls, input_array: Union[List[List[float]], np.ndarray]) -> 'M3':
        obj = np.asarray(input_array, dtype=np.float64).view(cls)
        if obj.shape != (3, 3):
            raise ValueError("Matrix3 must be a 3x3 matrix.")
        return obj

    def __repr__(self) -> str:
        return f"Matrix3(\n{super().__repr__()}\n)"

    def __str__(self) -> str:
        return f"Matrix3(\n{super().__str__()}\n)"
