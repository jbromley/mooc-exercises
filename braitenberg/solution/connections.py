from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")  # write your function instead of this one
    h, w = shape
    hw = w // 2
    mh = h // 2
    res[mh:, :hw] = 1
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")  # write your function instead of this one
    h, w = shape
    hw = w // 2
    mh  = h // 2
    res[mh:, hw:] = 1    
    return res
