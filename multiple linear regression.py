import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression

# Dataset
experience = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
education = np.array([10, 11, 12, 13, 14, 15, 16, 17]).reshape(-1, 1)
salary = np.array([2500, 3000, 4000, 4500, 5500, 6500, 7000, 8000])

# Combining independent variables
X = np.hstack((experience, education))

# Creating the model
model = LinearRegression()
model.fit(X, salary)

# Extracting coefficients and intercept
b0 = model.intercept_
b1, b2 = model.coef_

# Print results
print("The slope coefficients are:")
print(f"b1 (Experience): {b1:.2f}")
print(f"b2 (Education): {b2:.2f}")
print(f"Intercept (b0): {b0:.2f}")
print(f"Plane Equation: Salary = {b0:.2f} + ({b1:.2f})*Experience + ({b2:.2f})*Education")

# Plotting the data and regression plane
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(experience, education, salary, color='red', label='Actual Data')

# Creating a meshgrid for the plane
x1_range = np.linspace(min(experience), max(experience), 10)
x2_range = np.linspace(min(education), max(education), 10)
x1_mesh, x2_mesh = np.meshgrid(x1_range, x2_range)
y_pred = b0 + b1 * x1_mesh + b2 * x2_mesh

ax.plot_surface(x1_mesh, x2_mesh, y_pred, color='cyan', alpha=0.5)

# Labels and title
ax.set_xlabel("Experience (Years)")
ax.set_ylabel("Education (Years)")
ax.set_zlabel("Salary ($)")
ax.set_title("Multiple Linear Regression Plane")
ax.legend()

plt.show()

# Analysis
print("\nConclusion:")
if b1 > 0 and b2 > 0:
    print("Positive Relationship: As Experience and Education increase, Salary also increases.")
elif b1 < 0 or b2 < 0:
    print("Negative Relationship: Increase in one or both variables leads to a decrease in Salary.")
else:
    print("No significant relationship detected.")
