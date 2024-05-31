import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import time

x = sp.Symbol('x') # zmienna, po ktorej liczona jest pochodna
y = sp.cos(x) # funkcja
max_factor = 20 # maksymalny wspolczynnik - 1 ktory zostanie obliczony
a = 3 # punkt wokol ktorego odbywa sie aproksymacja

derivatives = []
derivative_values = []
coeffs = []

derivatives.append(y.diff(x))
for i in range(1, max_factor-1): # obliczenie pochodnych
    derivatives.append(derivatives[i-1].diff(x))

for i in range(max_factor-1): # obliczenie wartosci dla pochodnych w punkcie a
    f = sp.lambdify(x, derivatives[i], 'numpy')
    derivative_values.append(f(a))

#Tu zmienic funkcję (zamiast x -> a) z reguły na obliczenie współczynników
coeffs.append(sp.cos(a))
for i in range(1, max_factor-1): # obliczenie wspolczynnikow
    coeffs.append(derivative_values[i-1]/sp.factorial(i))

print("Pochodne:")
print(derivatives)
print("Wartosci pochodnych:")
print(derivative_values)
print("Wspolczynniki wielomianu:")
print(coeffs)

start = time.time()

density = 1000
D = np.linspace(-np.pi*2, np.pi*2, density)
vals = np.zeros(density)
for i in range(len(D)):
    for j in range(len(coeffs)-1):
        vals[i] += coeffs[j] * (D[i]-a)**j


end = time.time()
print(end-start)

#Tu tez zmienic funkcję (zamiast x -> D[i])
original_function_vals = []
for i in range(density):
    original_function_vals.append(sp.cos(D[i]))

plt.plot(D, original_function_vals, label="cos(x)")
plt.plot(D, vals, label=f'Taylor Series for {y}, factor = {max_factor}')
plt.ylim(-2,2)
plt.legend()
plt.show()






