Project #1: Wedding Cost Prediction (Linear Regression From Scratch)**.

# 💍 Wedding Cost Prediction — Linear Regression From Scratch

This project applies **machine learning fundamentals** to predict wedding costs using a fully custom implementation of **linear regression with gradient descent** (built from scratch using only NumPy).

It is part of my AI/ML learning journey, where I build foundational algorithms manually to deeply understand how models learn before transitioning to more advanced architectures (neural networks, transformers, MCP agents, and knowledge graphs).

---

## Project Overview

In this project, I:

* Built a **synthetic dataset** of 300 weddings with pricing (civil, elopements, local weddings, destination weddings).
* Performed **exploratory data analysis (EDA)** to understand distributions and relationships.
* Implemented **feature scaling**, **train/test split**, and **matrix-based predictions**.
* Built **linear regression from scratch** using:
  * Forward pass
  * Mean Squared Error (MSE)
  * Gradients (`dW`, `db`)
  * Gradient descent updates
* Unscaled learned weights to interpret their real-world meaning.
* Evaluated model performance using **Mean Absolute Error (MAE)** on unseen test data.

This is the first project in my ML portfolio

---

## 🔧 Technologies Used

* **Python**
* **NumPy**
* **Pandas**
* **Matplotlib**
* **Jupyter Notebook**

No machine learning libraries (like scikit-learn) were used to train the model — everything was implemented manually for learning purposes.

---

## 🧪 Dataset Description

The dataset simulates realistic wedding scenarios:

| Feature                | Description                                        |
| ---------------------- | -------------------------------------------------- |
| `wedding_type`         | civil, elopement, local venue, destination, resort |
| `guest_count`          | varies by wedding type (2–200+)                    |
| `decor_level`          | 1–5                                                |
| `flower_package_level` | 1–5                                                |
| `photographer_hours`   | 1–12                                               |
| `dress_budget`         | $300–$10,000                                       |
| `total_cost_usd`       | the target wedding cost                            |

Special rules were applied (e.g., elopements limited to 2–5 guests, civil weddings up to 10 guests, pricing caps, etc.).

Data located in:

```
/data/wedding_cost_dataset_v3.csv
```

---

## Model Architecture (From Scratch)

This project implements the classic linear regression equation:

```
y = XW + b
```

Where:

* **X** = feature matrix
* **W** = learned weights
* **b** = learned bias (base cost)
* **y** = predicted wedding cost

### Gradient Descent Steps

1. Compute predictions:

```
y_pred = X @ W + b
```

2. Compute error:

```
error = y_pred - y
```

3. Compute cost (MSE):

```
loss = (1/(2m)) * sum(error**2)
```

4. Compute gradients:

```
dW = (1/m) * X.T @ error
db = (1/m) * sum(error)
```

5. Update:

```
W -= alpha * dW
b -= alpha * db
```

The model was trained for **1000 iterations** with learning rate **0.01**.

---

## Training Loss Curve

The training notebook visualizes how the loss decreases over time, confirming successful gradient descent convergence.

---

## Results & Interpretation

### ✔ Learned Real-World Feature Impacts

Weights were unscaled to interpret the model in actual dollars.

Examples of insights (your notebook prints exact values):

* **guest_count** → $X added per additional guest
* **decor_level** → $Y added per upgrade in decor tier
* **flower_package_level** → $Z added per level
* **photographer_hours** → ~$A added per hour
* **dress_budget** → small positive influence per $1 spent

### ✔ Learned Bias (Base Cost)

The bias term represents the **baseline wedding cost** when all features are at their average levels.

This value was around **$40k–$45k**, matching realistic mid-range wedding pricing.

---

## Model Evaluation

Unseen data was evaluated using **Mean Absolute Error (MAE)**:

```
mae = np.mean(np.abs(y_test_pred - y_test))
```

This expresses predictive accuracy directly in **dollars**, making it easy to interpret:

> “On average, the model’s predictions are off by about $X.”

---

## Notebook

All implementation is contained in:

```
notebooks/01_wedding_cost_regression.ipynb
```

It includes:

* Data loading
* EDA
* Feature engineering
* Scaling
* Gradient descent
* Weight unscaling
* Model evaluation
* Loss plot

---

## 🚀 How to Run This Project

### 1. Clone the repo

```bash
git clone <your_repo_url>
cd wedding-cost-ml-regression
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install packages

```bash
pip install -r requirements.txt
```

(If you make one; otherwise install manually.)

### 4. Launch Jupyter Notebook

```bash
python -m notebook
```

Open:

```
notebooks/01_wedding_cost_regression.ipynb
```

---

## What I Learned

* How linear regression works under the hood
* Vectorized NumPy operations
* Matrix multiplication and dimensions
* Gradient descent intuition
* Feature scaling importance
* How to interpret model weights in the real world
* How to structure an ML project end-to-end

---

##  Next Steps (Portfolio Project 2)

➡️ Implement **Logistic Regression From Scratch**
➡️ Build a **Gradient Descent Visualizer**
➡️ Begin building ML & AI portfolio on GitHub
