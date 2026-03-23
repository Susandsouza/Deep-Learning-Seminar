import numpy as np

# Input and expected output
x = np.array([[2]])
y = np.array([[4]])

# Initialize weight
w = np.random.rand(1,1)

lr = 0.01

for i in range(100):
    y_pred = x * w
    loss = (y - y_pred)**2
    grad = -2 * x * (y - y_pred)
    w = w - lr * grad

print("Final weight:", w)
