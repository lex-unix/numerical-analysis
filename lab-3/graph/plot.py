from matplotlib import pyplot as plt

x = [14.4, 14.8, 15.2, 15.6, 16]
y = [16.4, 16.8, 17.2, 17.6, 18]
plt.style.use('seaborn-notebook')
plt.plot(x, y, label='Polynomial')
plt.title('Dataset graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()