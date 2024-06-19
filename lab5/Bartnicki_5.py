import numpy as np
import matplotlib.pyplot as plt

def newton_method(x0, stop):
    x_prev = None
    x_curr = x0
    iteration = 0

    while True:
        x_curr, x_prev = x_curr - f(x_curr) / df(x_curr), x_curr
        iteration += 1
        if stop(x_curr, x_prev):
            break
    return x_curr, iteration

def secant_method(x0, xn, stop):
    x1 = x0
    x2 = xn
    iteration = 0
    while True:
        x2, x1 = x2 - (x2 - x1) / (f(x2) - f(x1)) * f(x2), x2
        iteration += 1
        if stop(x2, x1):
            break
    return x2, iteration

def incremental(x1, x2):
    return abs(x1 - x2) < rho

def residual(x1, x2):
    return abs(f(x2)) < rho

def solve():
    start_points = np.linspace(a, b, 19)
    newton_answers = []
    print("\n\nRho: ", rho)
    for x0 in start_points:
        root, iterations = newton_method(x0, incremental)
        newton_answers.append((root, iterations))
    secant_a_answers = []
    secant_b_answers = []
    for x0 in start_points:
        if x0 != b:
            root, iterations = secant_method(x0, b, residual)
            secant_a_answers.append((root, iterations))
    for xn in start_points:
        if xn != a:
            root, iterations = secant_method(a, xn, residual)
            secant_b_answers.append((root, iterations))
    print("\nNewton")
    print(newton_answers)
    print("\nSecant (moving a)")
    print(secant_a_answers)
    print("\nSecant (moving b)")
    print(secant_b_answers)

f = lambda x: x ** 15 - (1 - x) ** 10
df = lambda x: 15 * x ** 14 + 10 * (1 - x) ** 9
a = 0.2
b = 2

#x0 = 0.56984
rhos = [1e-1, 1e-2, 1e-3, 1e-4, 1e-8, 1e-15]
for rho in rhos:
    solve()