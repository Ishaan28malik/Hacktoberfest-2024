import numpy as np


# Gaussian Elimination without partial pivoting for factorizing a
# linear system A x = b into A = L * U and b = L^{-1}x * b
#
# Inputs: Matrix A, Vector b
#
# Outputs: Modified matrix A containing L and U, Modified vector b
#
def GE(A, b):
    n = A.shape[0]
    M = np.eye(n)

    for k in range(0, n - 1):    # Loop over columns
        if A[k, k] == 0:    # Stop if pivot is zero
            raise RuntimeError("\nInput matrix is singular.")

        for i in range(k + 1, n):    # Loop over rows below digonal
            M[i, k] = A[i, k] / A[k, k]    # Multipliers for current column
            A[i, k] = M[i, k]    # Store L "in place" instead of 0
            for j in range(k + 1, n):    # Loop over non-zero columns
                A[i, j] -= M[i, k] * A[k, j]
                
            b[i] -= M[i, k] * b[k]    # Modify right hand side vector
            
    return A, b
