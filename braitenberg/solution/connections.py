from typing import Tuple

import numpy as np


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    h, w = shape
    kneept = w // 4
    knee_width = w // 4
    offpt = 3 * w // 8
    farpt = h // 2

    for x in range(0, kneept):
        res[farpt:, x] = x / knee_width
    res[farpt:, :offpt] = 1.0
    return res


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    h, w = shape
    onpt = 3 * w // 8
    knee_width = w // 4
    kneept = w - knee_width
    farpt = h // 2

    res[farpt:, onpt:kneept] = 1.0
    for x in range(kneept, w):
        res[farpt:, x] = 1.0 - (x - kneept) / knee_width

    return res
