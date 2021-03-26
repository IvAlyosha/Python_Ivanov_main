import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,4000)
plt.plot(x, x)
plt.plot(x, np.cos(10*x))
