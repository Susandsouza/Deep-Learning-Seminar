# 🧠 Backpropagation in ANN vs CNN vs RNN

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![NumPy](https://img.shields.io/badge/Library-NumPy-orange.svg)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen.svg)
![Level](https://img.shields.io/badge/Level-Beginner--Intermediate-yellow.svg)

---
Team Members:

Member 1: Susan

Member 2: Simran

## ✨ Overview

This project presents a clear and practical comparison of how **Backpropagation** works across three major neural network architectures:

- Artificial Neural Networks (ANN)
- Convolutional Neural Networks (CNN)
- Recurrent Neural Networks (RNN)

The focus is not just theory — but **understanding through simple, executable code**.


---

## 🧩 Architecture Intuition

### 🔹 ANN (Fully Connected)

```
Input → Hidden Layer → Output
   ● -------- ● -------- ●
```

✔ Direct connections  
✔ Simple gradient flow  

---

### 🔹 CNN (Spatial Learning)

```
Image → [Filter] → Feature Map → Output
        ⬛⬛⬛
        ⬛⬛⬛
```

✔ Learns patterns (edges, textures)  
✔ Uses shared weights (filters)  

---

### 🔹 RNN (Sequential Memory)

```
x₁ → [h] → x₂ → [h] → x₃ → [h]
         ↺      ↺      ↺
```

✔ Remembers previous inputs  
✔ Backpropagation through time  

---
## Backpropagation Overview
Backpropagation is the core learning algorithm used in neural networks to minimize error by updating weights using gradients.

It works in two main phases:
1. **Forward Pass** – Compute output
2. **Backward Pass** – Compute gradients and update weights

## 📐 Gradient Formula
The gradient measures how much the loss function changes with respect to weights.

General form:

∂L / ∂W = (∂L / ∂y) · (∂y / ∂W)

Where:
- L = Loss function  
- W = Weights  
- y = Output  

👉 Using chain rule:
δ = (y_actual − y_predicted) × f'(z)

This helps in propagating error backward through layers.

## ⚙️ Weight Update Rule

Weights are updated using Gradient Descent:

W_new = W_old − η · (∂L / ∂W)

Where:
- η (eta) = Learning rate  
- ∂L/∂W = Gradient  
---
## 🧠 Backpropagation in ANN

Backpropagation in Artificial Neural Networks (ANN) is used to minimize error by updating weights using gradient descent and the chain rule.

---

## 🔹 1. Forward Propagation

In forward propagation, input data passes through layers to produce an output.

**Formula:**

y = f(Wx + b)

Where:
- W = Weights  
- x = Input  
- b = Bias  
- f = Activation Function
- 
---

## 🔹 2. Loss Function

The loss function measures how far the predicted output is from the actual output.

**Mean Squared Error (MSE):**

L = (1/n) Σ (y_actual − y_predicted)²

👉 Goal: Minimize this loss

---

## 🔹 3. Gradient Computation (Chain Rule)

Gradients tell us how to adjust weights to reduce loss.

**Chain Rule:**

∂L/∂W = (∂L/∂y) × (∂y/∂W)

**Error term:**

δ = (y_actual − y_predicted) × f'(z)

---

## 🔹 4. Algorithm

**Step-by-step:**

1. Initialize weights randomly  
2. Perform forward propagation  
3. Compute loss  
4. Calculate gradients using chain rule  
5. Update weights using gradient descent  
6. Repeat until convergence  

---

## 🔹 5. Calculation Example

**Problem:**
Input x = 2, Expected output y = 4  

---

### Step 1: Initialize
W = 1 (random)  
Learning rate (η) = 0.01  

---

### Step 2: Forward Pass
y_pred = x × W = 2 × 1 = 2  

---

### Step 3: Loss
L = (4 − 2)² = 4  

---

### Step 4: Gradient
∂L/∂W = -2 × x × (y_actual − y_pred)

= -2 × 2 × (4 − 2)  
= -8  

---

### Step 5: Weight Update

W_new = W_old − η × gradient  

= 1 − (0.01 × -8)  
= 1.08  

---
👉 After multiple iterations, W → 2  

---
## 🧠 Backpropagation in CNN

Backpropagation in Convolutional Neural Networks (CNN) extends standard backpropagation by applying gradients over convolutional filters and spatial structures.

---

## 🔹 1. Convolutional Operation

CNNs use filters (kernels) to extract features from input data such as images.

**Formula:**

Feature Map = Input ⊗ Kernel

Where:
- ⊗ = Convolution operation  
- Kernel = Filter matrix  
- Output = Feature map  

---

## 🔹 2. Kernel Update Rule

Instead of updating individual weights like ANN, CNN updates **filter values (kernels)**.

**Update Rule:**

K_new = K_old − η · (∂L / ∂K)

Where:
- K = Kernel  
- η = Learning rate  
- ∂L/∂K = Gradient of loss w.r.t kernel  

---

## 🔹 3. Gradient Computation (Chain Rule)

Gradients are computed using the chain rule across convolution layers.

**Formula:**

∂L/∂K = Input ⊗ δ

Where:
- δ = Error propagated backward  
- Input = Input feature map  

---

## 🔹 4. Algorithm

**Step-by-step:**

1. Apply convolution using kernel  
2. Apply activation function (ReLU)  
3. Perform pooling (optional)  
4. Flatten output  
5. Pass through fully connected layer  
6. Compute loss  
7. Backpropagate error:
   - Fully connected layer  
   - Flatten layer  
   - Pooling layer  
   - Convolution layer  
8. Update kernel values  
9. Repeat until convergence  

---

## 🔹 5. Calculation Example

**Input (3×3 Image):**

[ 1  2  3 ]  
[ 4  5  6 ]  
[ 7  8  9 ]  

**Kernel (3×3):**

[ 1  0  -1 ]  
[ 1  0  -1 ]  
[ 1  0  -1 ]  

---
## EXAMPLE :
### Step 1: Convolution

Output = sum of element-wise multiplication:

= (1×1 + 2×0 + 3×-1)  
+ (4×1 + 5×0 + 6×-1)  
+ (7×1 + 8×0 + 9×-1)  

= (1 + 0 − 3)  
+ (4 + 0 − 6)  
+ (7 + 0 − 9)  

= -2 + -2 + -2 = **-6**

---

### Step 2: Loss (example)

Assume expected output = 0  

L = (0 − (-6))² = 36  

---

### Step 3: Gradient (intuition)

Gradient is calculated w.r.t each kernel element using input values.

Example:
∂L/∂K ≈ Input × error  

---

### Step 4: Kernel Update

K_new = K_old − η × gradient  

👉 Kernel values adjust to reduce error in next iteration  

---
## 🧠 Backpropagation in RNN

Backpropagation in Recurrent Neural Networks (RNN) is performed using **Backpropagation Through Time (BPTT)**, where gradients are propagated across time steps instead of layers.

---

## 🔹 1. Hidden State Equation

The hidden state stores information from previous time steps.

**Formula:**

h_t = f(W_hh · h_{t-1} + W_xh · x_t + b_h)

Where:
- h_t = current hidden state  
- h_{t-1} = previous hidden state  
- x_t = input at time t  
- W_hh = hidden-to-hidden weights  
- W_xh = input-to-hidden weights  
- b_h = bias  

---

## 🔹 2. Output Equation

The output at each time step depends on the hidden state.

**Formula:**

y_t = f(W_hy · h_t + b_y)

Where:
- y_t = output at time t  
- W_hy = hidden-to-output weights  
- b_y = bias  

---

## 🔹 3. Loss Function

Loss is calculated across all time steps.

**Example (MSE):**

L = Σ (y_actual_t − y_predicted_t)²

👉 Total loss = sum of losses over sequence

---

## 🔹 4. Backpropagation Through Time (BPTT)

Instead of normal backpropagation, RNN unfolds across time steps.

**Key Idea:**
- Network is expanded into multiple time steps  
- Gradients are computed at each step  
- Errors flow backward through time  

**Formula:**

δ_t = (δ_{t+1} · W_hh) × f'(h_t)

---
## ⚙️ How Backpropagation Differs

| Aspect | ANN | CNN | RNN |
|------|-----|-----|-----|
| Flow | Straight | Spatial | Temporal |
| Operation | Matrix Multiply | Convolution | Sequence Recurrence |
| Weight Sharing | ❌ No | ✅ Yes | ✅ Yes |
| Complexity | Low | Medium | High |

---

## 🧪 Project Structure

```
📁 deep_learning_seminar/
│
├── ann.py     # Basic backpropagation
├── cnn.py     # Convolution demo
├── rnn.py     # Sequential processing
└── README.md
```

---

## 🚀 Run Locally

```bash
git clone <your-repo-link>
cd deep_learning_seminar
python ann.py
python cnn.py
python rnn.py
```

---

## 📊 Sample Output

```
ANN → Final weight: [[1.99]]
CNN → Convolution Output: -6
RNN → Final hidden state: 0.87
```

---

## 🧠 Key Learning

> Backpropagation is not different —  
> **its path changes based on architecture**

- ANN → Direct gradient flow  
- CNN → Spatial gradient through filters  
- RNN → Time-based gradient flow (BPTT)  

---

## 📚 References

- GeeksforGeeks – Neural Networks & Backpropagation
  https://www.geeksforgeeks.org/machine-learning/backpropagation-in-neural-network/

---

## 👩‍💻 Author

SUSAN 

SIMRAN


B.Tech – Information Science Engineering  

