import numpy as np
import matplotlib.pyplot as plt

def new_x(x):
    return ((x + 7) / 14) * 2*np.pi - np.pi

def trigonometric_approximation(x, y, m):
    n = len(x)

    def calc_ak(k):
        return 2 / n * sum(y[i] * np.cos(k * x[i]) for i in range(n))
    
    def calc_bk(k):
        return 2 / n * sum(y[i] * np.sin(k * x[i]) for i in range(n))
    
    x = [new_x(val) for val in x]
    ak = [calc_ak(k) for k in range(m + 1)]
    bk = [calc_bk(k) for k in range(m + 1)]
    
    def f(x):
        x = new_x(x)
        sum = 0
        for k in range(1, m):
            sum += ak[k] * np.cos(k * x) + bk[k] * np.sin(k * x)
        return ak[0] / 2 + sum
    
    return f

def max_error(func):
    y = abs(func(x) - f(x))
    return max(y)

def square_error(func):
    y = sum((func(x) - f(x)) ** 2)/n
    return y

def approximation(x):
    nodes = np.linspace(min(x), max(x), n)

    func = trigonometric_approximation(nodes, f(nodes), degree)

    fig, ax = plt.subplots()
    ax.plot(x, func(x), color='blue', label="Aproksymacja")
    ax.plot(x, f(x), color = 'green', label="Zadana funkcja")
    ax.scatter(nodes, f(nodes), color='green', label="Węzły")
    ax.legend()
    ax.set_title("Aproksymacja trygonometryczna")
    ax.grid(True)
    plt.show()

    # global y_square_error_max, y_square_error_max_n, y_square_error_max_degree
    y_max_error = max_error(func)
    y_square_error = square_error(func)

    # if y_square_error < y_square_error_max:
    #     y_square_error_max = y_square_error
    #     y_square_error_max_n = n
    #     y_square_error_max_degree = degree


    print("Degree:", degree)
    print("Nodes:", n)
    print("Max error:", y_max_error)
    print("Square error:", y_square_error)


# y_square_error_max = 1000
# y_square_error_max_n = 0
# y_square_error_max_degree = 0
m = 10
k = 1
f = lambda x: x ** 2 - m * np.cos(np.pi * x / k)
x = np.linspace(-7, 7, 1000)


degree = 6
n = 13
approximation(x)
# for degree in range(2, 15):
#     for n in range(degree*2+1, 400):
#         print(degree)
#         approximation(x)
# print(y_square_error_max, y_square_error_max_degree, y_square_error_max_n)