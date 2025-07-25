import matplotlib.pyplot as plt

def gradient_descent(x, y, lr=0.01, epochs=1000):
    m, b = 0.0, 0.0
    n = len(x)

    for _ in range(epochs):
        y_pred = [m * xi + b for xi in x]
        error = [y[i] - y_pred[i] for i in range(n)]

        dm = -(2 / n) * sum(x[i] * error[i] for i in range(n))
        db = -(2 / n) * sum(error)

        m -= lr * dm
        b -= lr * db

    return m, b

def plot_regression(x, y, m, b):
    plt.scatter(x, y, label='Data points')
    line_x = [min(x), max(x)]
    line_y = [m * xi + b for xi in line_x]
    plt.plot(line_x, line_y, color='red', label='Regression line')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Simple Linear Regression (Gradient Descent)')
    plt.legend()
    plt.grid(True)
    plt.show()

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 8, 10, 11, 13, 15, 17, 19]

m, b = gradient_descent(x, y, lr=0.01, epochs=1000)
print("Learned model: y = {:.2f}x + {:.2f}".format(m, b))
plot_regression(x, y, m, b)