import numpy as np

def f_ackley(x):
    return -20*np.exp(-0.2*np.sqrt(0.5*(x[0]**2 + x[1]**2))) - np.exp(0.5*(np.cos(2*np.pi*x[0]) + np.cos(2*np.pi*x[1]))) + np.exp(1) + 20

def f_beale(x):
    term1 = (1.5 - x[0] + x[0]*x[1])**2
    term2 = (2.25 - x[0] + x[0]*x[1]**2)**2
    term3 = (2.625 - x[0] + x[0]*x[1]**3)**2
    return term1 + term2 + term3

def f_bukin(x):
    return 100 * np.sqrt(np.abs(x[1] - 0.01 * x[0]**2)) + 0.01 * np.abs(x[0] + 10)

def f_jorobas(x):
    return 2*x[0]**2 - 1.05*x[0]**4 + (x[0]**6)/6 + x[0]*x[1] + x[1]**2

def f_cruzada_bandeja(x):
    return -0.0001 * np.power(np.abs(np.sin(x[0]) * np.sin(x[1]) * np.exp(np.abs(100 - np.sqrt(x[0]**2 + x[1]**2))/np.pi)) + 1, 0.1)

def f_esfera(x):
    return x[0]**2 + x[1]**2

def f_facil(x):
    return -np.cos(x[0]) * np.cos(x[1]) * np.exp(-((x[0] - np.pi)**2 + (x[1] - np.pi)**2))

def f_levi(x):
    return (np.sin(3*np.pi*x[0]))**2 + (x[0] - 1)**2 * (1 + (np.sin(3*np.pi*x[1]))**2) + (x[1] - 1)**2 * (1 + (np.sin(2*np.pi*x[1]))**2)

def f_matias(x):
    return 0.26 * (x[0]**2 + x[1]**2) - 0.48 * x[0] * x[1]

def f_McCormick(x):
    return np.sin(x[0] + x[1]) + (x[0] * x[1])**2 - 1.5 * x[0] + 2.5 * x[1] + 1

def f_mesasoporte(x):
    return -np.abs(np.sin(x[0]) * np.cos(x[1]) * np.exp(np.abs(1 - np.sqrt(x[0]**2 + x[1]**2) / np.pi)))

def f_portahuevos(x):
    return -(x[1] + 47) * np.sin(np.sqrt(np.abs(x[0]/2 + x[1] + 47))) - x[0] * np.sin(np.sqrt(np.abs(x[0] - (x[1] + 47))))

def f_goldstein(x):
    term1 = (1 + (x[0] + x[1] + 1)**2 * (19 - 14*x[0] + 3*x[0]**2 - 14*x[1] + 6*x[0]*x[1] + 3*x[1]**2))
    term2 = (30 + (2*x[0] - 3*x[1])**2 * (18 - 32*x[0] + 12*x[0]**2 + 48*x[1] - 36*x[0]*x[1] + 27*x[1]**2))
    return term1 * term2

def f_restringida(x, A=10):
    n = len(x)
    return A*n + np.sum(x**2 - A*np.cos(2*np.pi*x))

def f_Schaffer04(x):
    return 0.5 + (np.cos(np.sin(np.abs(x[0]**2 - x[1]**2)))**2 - 0.5) / (1 + 0.001 * (x[0]**2 + x[1]**2))**2

def f_Schaffer(x):
    return 0.5 + (np.sin(x[0]**2 - x[1]**2)**2 - 0.5) / (1 + 0.001 * (x[0]**2 + x[1]**2))**2

def f_shequel(x, a, c):
    m = len(c)
    n = len(x)
    result = 0
    for i in range(m):
        inner_sum = 0
        for j in range(n):
            inner_sum += (x[j] - a[i, j])**2
        result += 1 / (c[i] + inner_sum)
    return result

def f_stand(x):
    return (x[0] + 2*x[1] - 7)**2 + (2*x[0] + x[1] - 5)**2

def f_himmelblau(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

def f_rosenbrock_restringida_cubica(x):
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2

def f_mishra(x):
    return np.sin(x[1]) * np.exp((1 - np.cos(x[0]))**2) + np.cos(x[0]) * np.exp((1 - np.sin(x[1]))**2) + (x[0] - x[1])**2

def f_rosenbrock_constrained(x):
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2

def f_simionescu(x):
    return 0.1 * x[0] * x[1]