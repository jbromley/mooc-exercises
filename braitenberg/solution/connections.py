from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    h, w = shape

    # Set the parameters for the reaction matrix
    x_mid = 17 * w // 32
    x_hi = w
    y_active = 3 * h // 8
    y_full = 7 * h // 8

    # Size of the active area of matrix
    h_active = y_full - y_active
    w_active = x_hi - x_mid

    for y in range(y_active, h):
        x_off = int(x_mid + w_active * (y - y_active) / h_active)
        res[y, x_mid:x_off] = 1.0
    res[y_full:, x_mid:] = 1.0

    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    h, w = shape

    # Set the parameters for the reaction matrix
    x_mid = 17 * w // 32
    x_lo = 0
    y_active = 3 * h // 8
    y_full = 7 * h // 8

    # Size of the active area of matrix
    h_active = y_full - y_active
    w_active = x_mid - x_lo

    for y in range(y_active, h):
        x_on = int(x_mid - w_active * (y - y_active) / h_active)
        res[y, x_on:x_mid] = 1.0
    res[y_full:, :x_mid] = 1.0

    return res
