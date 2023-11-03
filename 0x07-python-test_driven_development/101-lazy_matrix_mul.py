#!/usr/bin/python3
"""A module for adding numbers."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices."""
    mat_a = np.array(m_a)
    mat_b = np.array(m_b)
    return np.dot(mat_a, mat_b)
