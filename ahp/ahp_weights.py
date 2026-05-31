# ahp/ahp_weights.py

import numpy as np

def ahp_weights():
    a12 = np.random.triangular(2, 3, 4)
    a13 = np.random.triangular(3, 4, 5)
    a23 = np.random.triangular(2, 3, 4)

    A = np.array([
        [1, a12, a13],
        [1/a12, 1, a23],
        [1/a13, 1/a23, 1]
    ])

    eigvals, eigvecs = np.linalg.eig(A)
    w = np.real(eigvecs[:, np.argmax(eigvals)])

    return w / np.sum(w)