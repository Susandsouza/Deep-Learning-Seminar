import numpy as np

inputs = [1, 2, 3]

W = np.random.rand() #weight of i/p reandomly initialised
h = 0 #hidden state

for x in inputs:
    h = np.tanh(W * x + h)

print("Initial weight input :", W)
print("Final hidden state:", h)
