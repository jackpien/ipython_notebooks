import numpy as np
import matplotlib.pyplot as plt

def softmax(Y):
    eY = np.exp(Y)
    den = eY.sum(axis=0)
    return eY / den

scores = np.array([3.0, 1.0, 0.2])

x = np.arange(-2.0, 6.0, 0.1)
posits = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(posits).T, linewidth=2)
plt.show()

print "Intial score: " + str(scores)
print softmax(scores)

