import numpy as np
import time


def max_error(x, x_expected):
    return max(x - x_expected)

def gauss_elimination(a, b):
    x = np.zeros(n)

    start = time.time()

    for i in range(n):
        max_el = abs(a[i][i])
        max_row = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > max_el:
                max_el = abs(a[j][i])
                max_row = j
        
        a[[i, max_row]] = a[[max_row, i]]
        b[i], b[max_row] = b[max_row], b[i]
        
        for j in range(i + 1, n):
            if a[i][i] == 0:
                continue
            c = a[j][i] / a[i][i]
            a[j, i:] -= c * a[i, i:]
            b[j] -= c * b[i]
    
    
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / a[i][i]
        for k in range(i - 1, -1, -1):
            b[k] -= a[k][i] * x[i]
    end = time.time()
    #print("Time: ", end - start)
    return x

# Zadanie 1 --------------------------------------
# n = 14
# for n in range (2, 26):
#     a = np.zeros((n, n), dtype=np.float64)
#     for i in range(n):
#         for j in range(n):
#             if i == 0:
#                 a[i][j] = 1
#             else:
#                 a[i][j] = 1 / (i + j + 1)
#     x_expected = np.array([1 * (-1) ** i for i in range(n)], dtype=np.float64)
#     b = a @ x_expected
#     solution = gauss_elimination(a, b)
#     #print("Solution:", solution)
#     error = max_error(solution, x_expected)
#     print(np.linalg.cond(a))
#     #print(f"Error {n}: {error}")

# Zadanie 2 --------------------------------------
# n = 14
# for n in range (2, 26):
#     a = np.zeros((n, n), dtype=np.float64)
#     for i in range(n):
#         for j in range(n):
#             if j >= i:
#                 a[i][j] = 2 * (i + 1) / (j + 1)
#             else:
#                 a[i][j] = a[j][i]
#     x_expected = np.array([1 * (-1) ** i for i in range(n)], dtype=np.float64)
#     b = a @ x_expected
#     solution = gauss_elimination(a, b)
#     #print("Solution:", solution)
#     error = max_error(solution, x_expected)
#     #print(f"Error {n}: {error}")
#     #print(np.linalg.cond(a))

# Zadanie 3 -------------------
k = 7
m = 4
ns = [2, 5, 10, 50, 100, 200, 500, 1000, 1500, 2500, 5000, 10000]
for n in range (2, 26):
    a = np.zeros((n, n), dtype=np.float64)
    for i in range(n):
        a[i][i] = k
        if i != n-1:
            a[i][i+1] = 1 / (i + m + 1)
        if i != 0:
            a[i][i-1] = k / (i + m + 2)
    x_expected = np.array([1 * (-1) ** i for i in range(n)], dtype=np.float64)
    b = a @ x_expected
    #print(n)
    solution = gauss_elimination(a, b)
    #rint("Solution:", solution)
    error = max_error(solution, x_expected)
    #print(f"Error {n}: {error}")
    print(error)