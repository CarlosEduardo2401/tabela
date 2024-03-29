import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Criando dados para plotagem
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Criando a figura e o eixo 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotando o gráfico 3D
ax.plot_surface(x, y, z, cmap='viridis')

# Definindo rótulos dos eixos
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Exibindo o gráfico
plt.show()
