from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    h, w = shape
    onpt = w // 4
    offpt = 7 * w // 16
    farpt = h // 2

    res[farpt:, onpt:offpt] = 1.0

    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    h, w = shape
    onpt = 7 * w // 16
    offpt = 3 * w // 4
    farpt = h // 2

    res[farpt:, onpt:offpt] = 1.0

    return res
