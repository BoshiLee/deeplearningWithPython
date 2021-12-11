import matplotlib.pyplot as plt
import numpy as np


def step_func(x):
    return np.array(x > 0, dtype=int)


x = np.arange(-5.0, 5.0, 0.1) #從 -5 ~ 5 一階增加 0.1 的陣列
y = step_func(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()