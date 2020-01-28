import numpy as np
import sys
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

NUM_SAMPLE = int(sys.argv[1])

x = np.random.rand(NUM_SAMPLE)*10
y = -0.1 + 0.01 * x + np.random.normal(0.05, 0.05, NUM_SAMPLE)
mean = np.poly1d(np.polyfit(x, y, 1))(x)

x_mt_mean = x[y > mean]
y_mt_mean = y[y > mean]
x_le_mean = x[y <= mean]
y_le_mean = y[y <= mean]
plt.scatter(x_mt_mean, y_mt_mean)
plt.scatter(x_le_mean, y_le_mean)
plt.plot(x, mean, linestyle='solid')
plt.xlim(0, 10)
plt.ylim(-0.5, 0.5)
plt.grid(which='major')
plt.show()
plt.savefig('regression_towrd_mean.png')
