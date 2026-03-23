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

output = np.sum(image * kernel)

print("Convolution Output:", output)
