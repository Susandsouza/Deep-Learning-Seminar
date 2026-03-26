import numpy as np

# Simple image
image = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# Filter (edge detection)
kernel = np.array([
    [1,0,-1],
    [1,0,-1],
    [1,0,-1]
])

output = np.sum(image * kernel) #convolutional output 
gradient = np.ones_like(kernel) * 0.01 #creatig  g for each k 
learning_rate = 0.1
kernel = kernel - learning_rate * gradient # Updated moves it slightly in the opposite direction of the gradient.

print("Initial Kernel:", kernel)
print("Input Image:", image)
print("Convolution Output:", output)
print("\nUpdated Kernel:",kernel)

