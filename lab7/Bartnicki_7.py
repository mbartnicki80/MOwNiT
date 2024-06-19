import numpy as np
import time

def spectral_radius(A):
    eigenvalues = np.linalg.eigvals(A)
    return max(abs(eigenvalues))

def euclides_error(x, x_expected):
    return np.linalg.norm(x - x_expected)

def first_stop(x_next, x_curr):
    return np.linalg.norm(x_next - x_curr) < rho

def second_stop(A, x, b):
    return np.linalg.norm(A @ x - b) < rho

def jacob_method(A, b, x_start, stop=first_stop):
    diagonal = np.diag(A)
    rest = A - np.diagflat(diagonal)
    x_curr = x_start
    iterations = 0
    start = time.time()
    while 1:
        x_next = (b - (rest @ x_curr)) / diagonal
        iterations += 1
        if stop(x_next, x_curr):
            end = time.time()
            #print("Time: ", end - start)
            break
        x_curr = x_next
    return x_next, iterations

ns = [i for i in range(2, 26)]
ns.extend([50, 100, 500, 1000, 2000, 5000])
#ns = [2, 5, 10, 50, 100, 1000]
k = 11
m = 2
rhos = [1e-6]
#rhos = [1e-2, 1e-4, 1e-6, 1e-10, 1e-12]
rhos.reverse()
for rho in rhos:
    for n in ns:
        A = np.zeros((n, n), dtype=np.float64)
        for i in range(n):
            for j in range(n):
                if j == i:
                    A[i][j] = k
                else:
                    A[i][j] = m / (n - i - j + 0.5 + 2)
        x_expected = np.array([1 * (-1) ** i for i in range(n)], dtype=np.float64)
        b = A @ x_expected
        x_start = np.zeros(n)
        #x_start = np.array([100 for _ in range(n)], dtype=np.float64)

        # D_inv = np.diag(1 / np.diag(A))
        # L_plus_U = A - np.diagflat(np.diag(A))
        # B = D_inv @ L_plus_U
        # radius = spectral_radius(B)
        # print(n, radius)

        solution, iterations = jacob_method(A, b, x_start)
        #print("Solution:", solution)
        error = euclides_error(solution, x_expected)
        #print("n: ", n, "Error: ", error, "Iterations: ", iterations)
        print(error)