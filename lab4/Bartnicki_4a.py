import numpy as np
import matplotlib.pyplot as plt

def least_squares_approximation(x, y, degree): #zakladam wagi = 1
    A = np.zeros((degree + 1, degree + 1))
    b = np.zeros(degree + 1)

    for i in range(degree + 1):
        for j in range(degree + 1):
            A[i][j] = np.sum(x ** (i + j))

    for i in range(degree + 1):
        b[i] = np.sum(y * x ** i)

    coefficients = np.linalg.solve(A, b)
    return coefficients

def evaluate_polynomial(coefficients, x):
    y = np.zeros_like(x)
    for i, coeff in enumerate(coefficients):
        y += coeff * x ** i
    return y

def max_error(f_natural, f_values):
    y = abs(f_natural - f_values)
    return max(y)

def square_error(f_natural, f_values):
    y = np.sum((f_natural - f_values) ** 2) / len(x)
    return y

def approximation(x):
    nodes = np.linspace(min(x), max(x), n)
    f_values = f(nodes)
    
    coefficients = least_squares_approximation(nodes, f_values, degree)
    y_values = evaluate_polynomial(coefficients, x)

    # fig, ax = plt.subplots()
    # ax.plot(x, y_values, color='blue', label="Approximation")
    # ax.plot(x, f(x), color = 'green', label="Given function")
    # ax.scatter(nodes, f(nodes), color='green', label="Nodes")
    # ax.legend()
    # ax.set_title("Least squares Approximation")
    # ax.grid(True)
    # plt.show()
    f1 = f(x)
    global y_square_error_max, y_square_error_max_n, y_square_error_max_degree
    y_max_error = max_error(y_values, f1)
    y_square_error = square_error(y_values, f1)

    if y_square_error < y_square_error_max:
        y_square_error_max = y_square_error
        y_square_error_max_n = n
        y_square_error_max_degree = degree


    print("Degree:", degree)
    print("Nodes:", n)
    print("Max error:", y_max_error)
    print("Square error:", y_square_error)

y_square_error_max = 100
y_square_error_max_n = 0
y_square_error_max_degree = 0
m = 10
k = 1
f = lambda x: x ** 2 - m * np.cos(np.pi * x / k)
x = np.linspace(-7, 7, 1000)


for degree in range(1, 180):
    for n in range(degree+1, 200):
        approximation(x)

print(y_square_error_max, y_square_error_max_n, y_square_error_max_degree)
# degree = 35
# n = 150
# approximation(x)