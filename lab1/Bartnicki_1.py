import numpy as np

roots = [i for i in range(1, 21)]
coefficients = np.poly(roots)
#coefficients_array = np.array(coefficients, dtype=np.float32)
coefficients_array = np.array(coefficients, dtype=np.float64)
#coefficients_array = np.array(coefficients, dtype=np.float128)

print("Coefficients:\n", list(coefficients))

print("Roots:\n", np.roots(coefficients_array))

def horner(x):
    value = coefficients[-1]
    for i in range(len(coefficients_array)-2, -1, -1):
        value = value * x + coefficients_array[i]
    return value

def divide_and_conquer(coefficients, x):
    n = len(coefficients)
    if n==1:
        return coefficients[0]
    mid = n // 2
    left = coefficients[mid:]
    right = coefficients[:mid]

    return divide_and_conquer(left, x) + pow(x, mid) * divide_and_conquer(right, x)

print("Value at 1 (Horner's method): ", horner(1))
print("Value at 20 (Horner's method): ", horner(20))
print("Value at 1 (Divide and conquer): ", divide_and_conquer(coefficients_array, 1))
print("Value at 20 (Divide and conquer): ", divide_and_conquer(coefficients_array, 20))