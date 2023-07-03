import numpy as np
""" function to multiply matrices """


def lazy_matrix_mul(m_a, m_b):
    """ def lazy_matrix_mul(m_a, m_b): mul 2 matrices """
    l1 = np.array(m_a)
    l2 = np.array(m_b)
    l3 = np.dot(l1, l2)
    return l3
