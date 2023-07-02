#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_a or len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if not m_b or len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for i in m_a:
        if not all(isinstance(x, (int, float)) for x in i):
            raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        if not all(isinstance(x, (int, float)) for x in i):
            raise TypeError("m_b should contain only integers or floats")
    length = len(m_a[0])
    if not all(len(i) == length for i in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(i) == length for i in m_b):
        raise TypeError("each row of m_b must be of the same size")
    l1 = []
    for i in m_b:
        new_matrix = list(zip(*m_b))
    for i in m_a:
        for y in new_matrix:
            l1.append(list(map(lambda x, z: x * z, i, y)))
    l2 = []
    new_list = []
    for i in l1:
        l2.append(sum(i))
        if len(m_b) == len(l2):
            new_list.append(l2)
            l2 = []
    return new_list
