import numpy as np

# Input and expected output
x = np.array([[2]])
y = np.array([[4]])

# Initialize weight
w = np.random.rand(1,1)

lr = 0.01  #learning rate 

for i in range(100):
    y_pred = x * w      # forward propogation 
    loss = (y - y_pred)**2   # loss error using mse
    grad = -2 * x * (y - y_pred) # gradient
    w = w - lr * grad # update weight

print("InitialWeight:", w)
print("Loss:", loss)
print("Predicted Output:", y_pred)
print("Gradient:", grad)

