import numpy as np
import matplotlib.pyplot as plt

x = np.array([-1.6000, -1.2000, -0.8000, -0.4000, 0, 0.4000, 0.8000, 1.2000, 1.6000, 2.0000])
x = [1 + value for value in x]
y = [0.04 + value for value in x]
A = np.vstack([x, np.ones(len(x))]).T
print(A)

m, c = np.linalg.lstsq(A, y, rcond=None)[0]
print(m, c)

plt.plot(x, y, 'o', color='b', label='Запропоновані значення', markersize=10)
plt.plot(x, m * x + c, 'r', label='Отримана лінія', markersize=5)
plt.title('Пряма лінія y = Ax + b')
plt.legend()
plt.show()