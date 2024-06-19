import numpy as np
import time

def max_error(x, x_expected):
    return max(x - x_expected)

def thomas_algorithm(a, b, c, d):
    c_prim = np.zeros(n)
    d_prim = np.zeros(n)
    x = np.zeros(n)

    start = time.time()
    c_prim[0] = c[0] / b[0]
    d_prim[0] = d[0] / b[0]

    for i in range(1, n):
        denom = b[i] - a[i] * c_prim[i - 1]
        c_prim[i] = c[i] / denom
        d_prim[i] = (d[i] - a[i] * d_prim[i - 1]) / denom

    
    x[-1] = d_prim[-1]

    for i in range(n - 2, -1, -1):
        x[i] = d_prim[i] - c_prim[i] * x[i + 1]
    end = time.time()
    #print("Time: ", end - start)

    return x

k = 7
m = 4
ns = [2, 5, 10, 50, 100, 200, 500, 1000, 1500, 2500, 5000, 10000]
for n in range (2, 26):
    a = np.zeros(n, dtype=np.float64)
    b = np.zeros(n, dtype=np.float64)
    c = np.zeros(n, dtype=np.float64)
    for i in range(n):
        b[i] = k
        if i != n-1:
            c[i] = 1 / (i + m + 1)
        if i != 0:
            a[i] = k / (i + m + 2)
    x_expected = np.array([1 * (-1) ** i for i in range(n)], dtype=np.float64)
    d = (np.diag(b) + np.diag(a[1:], -1) + np.diag(c[:-1], 1)) @ x_expected
    #print(n)
    solution = thomas_algorithm(a, b, c, d)
    #print("Solution:", solution)
    error = max_error(solution, x_expected)
    #print(f"Error {n}: {error}")
    print(error)