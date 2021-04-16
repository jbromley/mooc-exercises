from typing import Tuple

import numpy as np


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")  # write your function instead of this one
    h, w = shape
    left_knee = w // 4
    right_knee = 3 * w // 4
    res[:, 0:left_knee] = 1
    for x in range(left_knee, right_knee):
        res[:, x] = 1 - 2 * (x - left_knee) / (right_knee - left_knee)
    res[:, right_knee:w] = -1
    return res


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")  # write your function instead of this one
    h, w = shape
    left_knee = w // 4
    right_knee = 3 * w // 4
    res[:, 0:left_knee] = -1
    for x in range(left_knee, right_knee):
        res[:, x] = -1 + 2 * (x - left_knee) / (right_knee - left_knee)
    res[:, right_knee:w] = 1
    return res
