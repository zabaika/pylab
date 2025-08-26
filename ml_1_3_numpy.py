import numpy as np


def normalize(m):
    mean = np.mean(m, 0)
    st = np.std(m, 0)
    m_norm = (m - mean) / st
    print(m_norm)


def elements(m):
    summa = np.sum(m, 1)
    print((np.nonzero(summa > 10)))


def singles(m1, m2):
    print(m1)
    print(m2)
    final = np.vstack((m1, m2))
    print(final)


matrix = np.random.normal(1, 10, (1000, 50))
el_matrix = np.array([[4, 5, 0],
                      [1, 9, 3],
                      [5, 1, 1],
                      [3, 3, 3],
                      [9, 9, 9],
                      [4, 7, 1]])
first_matrix = np.eye(3)
second_matrix = np.eye(3)
# normalize(matrix)
# elements(el_matrix)
# singles(first_matrix,second_matrix)
