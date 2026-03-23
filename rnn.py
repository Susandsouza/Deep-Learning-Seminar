import numpy as np

inputs = [1, 2, 3]

W = np.random.rand()
h = 0

for x in inputs:
    h = np.tanh(W * x + h)

print("Final hidden state:", h)
