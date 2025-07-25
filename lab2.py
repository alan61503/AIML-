import matplotlib.pyplot as plt

# Prediction function
def predict(X, b):
    return [b[0] + b[1] * x1 + b[2] * x2 for x1, x2 in X]

# Gradient computation
def compute_gradients(X, y, b):
    n = len(X)
    db0 = db1 = db2 = 0

    for i in range(n):
        x1, x2 = X[i]
        y_pred = b[0] + b[1] * x1 + b[2] * x2
        error = y_pred - y[i]
        db0 += error
        db1 += error * x1
        db2 += error * x2

    db0 *= 2/n
    db1 *= 2/n
    db2 *= 2/n

    return db0, db1, db2

# Gradient descent for multiple linear regression
def gradient_descent_multi(X, y, lr=0.01, epochs=1000):
    b = [0.0, 0.0, 0.0]  # Intercept, coef1, coef2
    for _ in range(epochs):
        db0, db1, db2 = compute_gradients(X, y, b)
        b[0] -= lr * db0
        b[1] -= lr * db1
        b[2] -= lr * db2
    return b  # ← FIXED indentation

# Sample data
X = [
    [1, 2], [2, 3], [3, 4], [4, 5], [5, 6],
    [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]
]
y = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# Run gradient descent
coeffs = gradient_descent_multi(X, y, lr=0.01, epochs=1000)
print("Learned Coefficients:", coeffs)

# Make predictions
y_pred = predict(X, coeffs)

# Plot actual vs predicted
plt.scatter(range(len(y)), y, label='Actual', color='blue')
plt.plot(range(len(y_pred)), y_pred, label='Predicted', color='green')
plt.xlabel('Sample Index')
plt.ylabel('Target')
plt.title('Multiple Linear Regression via Gradient Descent')
plt.legend()
plt.grid(True)
plt.show()