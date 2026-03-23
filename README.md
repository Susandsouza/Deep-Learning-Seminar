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

## 🧭 Why This Project?

Understanding backpropagation is easy in ANN.  
But things change when:

- 📸 Spatial data → CNN  
- 🔁 Sequential data → RNN  

This project helps you **see those differences clearly**.

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

---

## 👩‍💻 Author

Mini Seminar Project  
B.Tech – Information Science Engineering  

