import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset
height = np.array([150, 160, 170, 180, 190, 200, 210, 220]).reshape(-1, 1)
weight = np.array([50, 55, 60, 65, 70, 75, 80, 85])

# Create Linear Regression Model
model = LinearRegression()
model.fit(height, weight)

# Calculate slope and intercept
slope = model.coef_[0]
intercept = model.intercept_
print("The slope is:", slope)
print("The intercept is:", intercept)

# Equation of the line
print(f"Equation of the Line: y = {slope:.2f}x + {intercept:.2f}")

# Predict values for regression line
height_range = np.linspace(140, 230, 100).reshape(-1, 1)
predicted_weight = model.predict(height_range)

# Plot the data and regression line
plt.scatter(height, weight, color='red', label='Original Data')
plt.plot(height_range, predicted_weight, color='blue', label='Regression Line')
plt.xlabel("Height (cm)")
plt.yalabel("Weight (kg)")
plt.title("Simple Linear Regression: Height vs Weight")
plt.legend()
plt.grid(True)
plt.show()

# Conclusion
print("Conclusion: There is a strong positive relationship between height and weight.")
