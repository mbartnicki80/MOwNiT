import numpy as np
import matplotlib.pyplot as plt

def hermite_interpolation(nodes):
    m = n * 2
    
    nodes_ = []
    for i in range(n):
        nodes_.append(nodes[i])
        nodes_.append(nodes[i])

    matrix = np.zeros((m, m))

    for i in range(m):
        matrix[i][0] = f(nodes_[i])

    for i in range(m):
        for j in range(1, i + 1):
            if j == 1 and i % 2 == 1:
                 matrix[i][j] = f_der(nodes_[i])
            else:
                matrix[i][j] = (matrix[i][j-1] - matrix[i-1][j-1]) / (nodes_[i] - nodes_[i-j])
            
            
    coeff = [matrix[i][i] for i in range(m)]

    def func(x):
        y = coeff[0]
        poly = 1
        curr_deg = 0
        for i in range(n):
            for _ in range(2):
                curr_deg += 1
                poly *= x - nodes[i]
                y += coeff[curr_deg] * poly
                if curr_deg == m - 1:
                    return y
                
    return func


def chebyshev(a, b, n):
    k = np.arange(1, n + 1)
    nodes = 0.5 * (a+b) + 0.5 * (b-a) * np.cos((2*k-1) * np.pi / (2*n))
    return nodes

def max_error(func):
    y = abs(func(x) - f(x))
    return max(y)

def square_error(func):
    y = sum((func(x) - f(x)) ** 2)/n
    return y

def interpolation(x, interpolation_func):
    nodes = np.linspace(min(x), max(x), n)
    nodes_cheb = chebyshev(min(x), max(x), n)

    func = interpolation_func(nodes)
    func_cheb = interpolation_func(nodes_cheb)

    fig, ax = plt.subplots(1, 2)
    
    ax[0].plot(x, func(x), color='red', label="Przyblizona funkcja")
    ax[0].plot(x, f(x), color = 'green', label="Zadana funkcja")
    ax[1].plot(x, func_cheb(x), color='red')
    ax[1].plot(x, f(x), color = 'green')
    ax[0].scatter(nodes, f(nodes), color='green', label="Wezly")
    ax[1].scatter(nodes_cheb, f(nodes_cheb), color='green')
    ax[0].legend()
    ax[0].set_title("Rownomiernie rozmieszczone wezly")
    ax[1].set_title("Wezly w zerach Czebyszewa")
    ax[0].grid(True)
    ax[1].grid(True)
    plt.show()

    y_max_error = max_error(func)
    y_max_error_cheb = max_error(func_cheb)
    y_square_error = square_error(func)
    y_square_error_cheb = square_error(func_cheb)

    print(n)
    print("Max error: ", y_max_error, y_max_error_cheb)
    print("Square error: ", y_square_error, y_square_error_cheb)

m = 10
k = 1
f = lambda x: x**2 - m * np.cos(np.pi * x / k)
f_der = lambda x: 2*x + (m * np.pi / k) * np.sin(np.pi * x / k)
x = np.linspace(-7, 7, 1000)

n = 35
interpolation(x, hermite_interpolation)
# for n in range(2, 41):
#     interpolation(x, hermite_interpolation)