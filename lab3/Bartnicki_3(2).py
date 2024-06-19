import numpy as np
import matplotlib.pyplot as plt

def spline_cubic_interpolation(h, f_values, boundaries=None):
    b = np.zeros(n-1)
    c = np.zeros(n-1)
    d = np.zeros(n-1)
    
    v = np.zeros(n)
    for i in range(1, n-1):
        v[i] = ((f_values[i+1] - f_values[i]) / h) - ((f_values[i] - f_values[i-1]) / h)

    A = np.zeros((n, n))
    for i in range(1, n-1):
        A[i][i-1] = h
        A[i][i] = 4 * h
        A[i][i+1] = h

    if boundaries == "natural":
        A[0][0] = A[-1][-1] = 2
    else:
        A[0][1] = A[-1][-1] = 1
        A[0][0] = A[-1][-2] = 2
    
    sigma = np.linalg.solve(A, v)

    for i in range(n-1):
        b[i] = (f_values[i+1] - f_values[i]) / h - h * (sigma[i+1] + 2 * sigma[i])
        c[i] = 3 * sigma[i]
        d[i] = (sigma[i+1] - sigma[i]) / h

    return b, c, d

def cubic_spline(b, c, d, nodes, f_values, x):
    for i in range(n - 1):
        if nodes[i] <= x <= nodes[i + 1]:
            return f_values[i] + b[i] * (x - nodes[i]) + c[i] * (x - nodes[i]) ** 2 + d[i] * (x - nodes[i]) ** 3
        
def max_error(f_natural, f_values):
    y = abs(f_natural - f_values)
    return max(y)

def square_error(f_natural, f_values):
    y = np.sum((f_natural - f_values) ** 2) / len(x)
    return y

def interpolation(x):
    nodes = np.linspace(min(x), max(x), n)
    f_values = f(nodes)
    h = nodes[1] - nodes[0]

    fig, ax = plt.subplots()
    b1, c1, d1 = spline_cubic_interpolation(h, f_values, "natural")
    b2, c2, d2 = spline_cubic_interpolation(h, f_values)

    f_natural = [cubic_spline(b1, c1, d1, nodes, f_values, xi) for xi in x]
    f_clamped = [cubic_spline(b2, c2, d2, nodes, f_values, xi) for xi in x]
    ax.plot(x, f_natural, color='red', label="Natural spline")
    ax.plot(x, f_clamped, color='blue', label="Clamped spline")
    ax.plot(x, f(x), color = 'green', label="Given function")
    ax.scatter(nodes, f(nodes), color='green', label="Nodes")
    ax.legend()
    ax.set_title("Cubic Spline Interpolation")
    ax.grid(True)
    plt.show()
    f1 = f(x)
    # global y_square_error_natural_max, y_square_error_clamped_max_i, y_square_error_natural_max_i, y_square_error_clamped_max
    y_max_error_natural = max_error(f_natural, f1)
    y_square_error_natural = square_error(f_natural, f1)
    y_max_error_clamped = max_error(f_clamped, f1)
    y_square_error_clamped = square_error(f_clamped, f1)

    # if y_square_error_natural < y_square_error_natural_max:
    #     y_square_error_natural_max = y_square_error_natural
    #     y_square_error_natural_max_i = n
    # if y_square_error_clamped < y_square_error_clamped_max:
    #     y_square_error_clamped_max = y_square_error_clamped
    #     y_square_error_clamped_max_i = n

    print(n)
    print("Max error natural: ", y_max_error_natural)
    print("Square error natural: ", y_square_error_natural)
    print("Max error clamped: ", y_max_error_clamped)
    print("Square error clamped: ", y_square_error_clamped)

# y_square_error_natural_max = 1000
# y_square_error_natural_max_i = 0
# y_square_error_clamped_max = 100
# y_square_error_clamped_max_i = 0
m = 10
k = 1
f = lambda x: x ** 2 - m * np.cos(np.pi * x / k)
x = np.linspace(-7, 7, 1000)
n = 3
interpolation(x)
# print(y_square_error_natural_max, y_square_error_natural_max_i)
# print(y_square_error_clamped_max, y_square_error_clamped_max_i)