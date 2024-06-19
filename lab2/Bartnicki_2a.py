import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(nodes):

    def L(xi, j):
        y = f(nodes[j])
        for i in range(n):
            if j != i:
                y *= (xi - nodes[i]) / (nodes[j] - nodes[i])
        return y
    
    return np.array([sum(L(xi, j) for j in range(n)) for xi in x])

def newton_coefficients(nodes):
    coefficients = [f(node) for node in nodes]
    
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coefficients[i] = (coefficients[i] - coefficients[i-1]) / (nodes[i] - nodes[i-j])
    
    return coefficients

def newton_interpolation(nodes):
    a = newton_coefficients(nodes)

    def N(xi):
        p = a[n-1]
        for k in range(1,n):
            p = a[n-k-1] + (xi - nodes[n-k-1])*p
        return p

    return [N(xi) for xi in x]

def chebyshev(a, b, n):
    k = np.arange(1, n + 1)
    nodes = 0.5 * (a+b) + 0.5 * (b-a) * np.cos((2*k-1) * np.pi / (2*n))
    return nodes

def max_error(y_nodes):
    y = abs(y_nodes - f(x))
    return max(y)

def square_error(y_nodes):
    y = sum((y_nodes - f(x)) ** 2)/n
    return y

def interpolation(x, interpolation_func):
    nodes = np.linspace(min(x), max(x), n)
    nodes_cheb = chebyshev(min(x), max(x), n)
    y_nodes = interpolation_func(nodes)
    y_nodes_cheb = interpolation_func(nodes_cheb)

    fig, ax = plt.subplots(1, 2)
    
    ax[0].plot(x, y_nodes, color='red', label="Przyblizona funkcja")
    ax[0].plot(x, f(x), color = 'green', label="Zadana funkcja")
    ax[1].plot(x, y_nodes_cheb, color='red')
    ax[1].plot(x, f(x), color = 'green')
    ax[0].scatter(nodes, f(nodes), color='green', label="Wezly")
    ax[1].scatter(nodes_cheb, f(nodes_cheb), color='green')
    ax[0].legend()
    ax[0].set_title("Rownomiernie rozmieszczone wezly")
    ax[1].set_title("Wezly w zerach Czebyszewa")
    ax[0].grid(True)
    ax[1].grid(True)
    plt.show()

    print(y_nodes)
    y_max_error = max_error(y_nodes)
    y_max_error_cheb = max_error(y_nodes_cheb)
    y_square_error = square_error(y_nodes)
    y_square_error_cheb = square_error(y_nodes_cheb)

    # global max_err_i, max_err, max_err_cheb, max_err_cheb_i

    # if y_square_error<max_err:
    #     max_err = y_square_error
    #     max_err_i = len(nodes)
    # if y_square_error_cheb<max_err_cheb:
    #     max_err_cheb = y_square_error_cheb
    #     max_err_cheb_i = len(nodes)

    print(n)
    print("Max error: ", y_max_error, y_max_error_cheb)
    print("Square error: ", y_square_error, y_square_error_cheb)

# max_err = 1000000
# max_err_i = 0
# max_err_cheb = 1000000
# max_err_cheb_i = 0

m = 10
k = 1
f = lambda x: x**2 - m * np.cos( np.pi * x / k)

x = np.linspace(-7, 7, 1000)

n = 67
interpolation(x, newton_interpolation)


# for n in range(30, 70):
#     interpolation(x, newton_interpolation)
# print(max_err, max_err_i)
# print(max_err_cheb, max_err_cheb_i)