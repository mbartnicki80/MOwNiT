import numpy as np
import matplotlib.pyplot as plt

def spline_quadratic_interpolation(f_values, nodes, boundaries=None):
    A = np.zeros((3 * n - 3, 3 * n - 3))
    v = np.zeros(3 * n - 3)

    if boundaries == "natural":
        A[-1][0] = 2
        v[-1] = 0
    else:
        A[-1][0] = 2 
        v[-1] = 2*(f_values[1] - f_values[0]) / (nodes[1] - nodes[0])

    A[0][0] = nodes[0]**2
    A[0][1] = nodes[0]
    A[0][2] = 1
    v[0] = f_values[0]
    v[2 * (n-1) - 1] = f_values[n-1]
    A[2 * (n-1) - 1][-3] = nodes[n-1]**2
    A[2 * (n-1) - 1][-2] = nodes[n-1]
    A[2 * (n-1) - 1][-1] = 1
    

    for i in range(1, n-1):
        v[i*2 - 1] = f_values[i]
        v[i*2] = f_values[i]
        A[i*2 - 1][i*3 - 3] = nodes[i]**2
        A[i*2 - 1][i*3 - 2] = nodes[i]
        A[i*2 - 1][i*3 - 1] = 1
        A[i*2][i*3] = nodes[i]**2
        A[i*2][i*3 + 1] = nodes[i]
        A[i*2][i*3 + 2] = 1
    j = 0
    for i in range(2*(n-1), len(A)-1):
        A[i][j*3] = 2 * nodes[j+1]
        A[i][j*3+1] = 1
        A[i][j*3+3] = - 2 * nodes[j+1]
        A[i][j*3+4] = -1
        j += 1

    coeffs = np.linalg.solve(A, v)
    a = np.zeros(n-1)
    b = np.zeros(n-1)
    c = np.zeros(n-1)

    for i in range(n-1):
        a[i] = coeffs[i*3]
        b[i] = coeffs[i*3 + 1]
        c[i] = coeffs[i*3 + 2]

    return a, b, c

def quadratic_spline(a, b, c, nodes, x):
    for i in range(n - 1):
        if nodes[i] <= x <= nodes[i + 1]:
            return c[i] + b[i] * x + a[i] * x ** 2
        
def max_error(f_natural, f_values):
    y = abs(f_natural - f_values)
    return max(y)

def square_error(f_natural, f_values):
    y = np.sum((f_natural - f_values) ** 2) / len(x)
    return y

def interpolation(x):
    nodes = np.linspace(min(x), max(x), n)
    f_values = f(nodes)

    fig, ax = plt.subplots()
    a1, b1, c1 = spline_quadratic_interpolation(f_values, nodes, "natural")
    a2, b2, c2 = spline_quadratic_interpolation(f_values, nodes)

    f_natural = [quadratic_spline(a1, b1, c1, nodes, xi) for xi in x]
    f_clamped = [quadratic_spline(a2, b2, c2, nodes, xi) for xi in x]
    ax.plot(x, f_natural, color='blue', label="a1 = 0")
    ax.plot(x, f_clamped, color='red', label="a1 = f'(x0) ")
    ax.plot(x, f(x), color = 'green', label="Given function")
    ax.scatter(nodes, f_values, color='green', label="Nodes")
    ax.legend()
    ax.set_title("Quadratic Spline Interpolation")
    ax.grid(True)
    plt.show()
    f1 = f(x)
    y_max_error_natural = max_error(f_natural, f1)
    y_square_error_natural = square_error(f_natural, f1)
    y_max_error_clamped = max_error(f_clamped, f1)
    y_square_error_clamped = square_error(f_clamped, f1)

    print(n)
    print("Max error natural: ", y_max_error_natural)
    print("Square error natural: ", y_square_error_natural)
    print("Max error clamped: ", y_max_error_clamped)
    print("Square error clamped: ", y_square_error_clamped)


m = 10
k = 1
f = lambda x: x ** 2 - m * np.cos(np.pi * x / k)
x = np.linspace(-7, 7, 1000)

n = 21
interpolation(x)
#interpolation(x)