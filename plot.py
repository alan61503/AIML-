import matplotlib.pyplot as plt
import numpy as np

# Task 1: Bar Chart
fig, ax = plt.subplots()
categories = ['A', 'B', 'C', 'D']
values = [25, 40, 35, 50]
ax.bar(categories, values, color=['red', 'blue', 'green', 'orange'])
ax.set_title("Bar Chart Example")
ax.set_xlabel("Categories")
ax.set_ylabel("Values")
ax.grid(True)
fig.show()

# Task 2: Pie Chart
fig, ax = plt.subplots()
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [45, 30, 15, 10]
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, explode=[0.1, 0, 0, 0])
ax.set_title("Programming Language Popularity")
plt.show()

# Task 3: Histogram
ages = [22, 23, 25, 27, 29, 35, 36, 40, 42, 45, 50, 52, 55, 58]
plt.hist(ages, bins=5, color='purple', edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age Groups")
plt.ylabel("Frequency")
plt.show()

# Task 4: Stack Plot
fig, ax = plt.subplots()
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
product_a = [20, 30, 40, 50]
product_b = [15, 25, 35, 45]
ax.stackplot(quarters, product_a, product_b, labels=['Product A', 'Product B'], colors=['lightblue', 'lightgreen'])
ax.set_title("Quarterly Sales of Products")
ax.set_xlabel("Quarters")
ax.set_ylabel("Sales")
ax.legend()
fig.show()

# Task 5: Area Chart
fig, ax = plt.subplots()
years = [2010, 2011, 2012, 2013, 2014]
production = [100, 120, 150, 180, 200]
ax.fill_between(years, production, color='cyan', alpha=0.5)
ax.set_title("Production Growth Over Years")
ax.set_xlabel("Year")
ax.set_ylabel("Production")
plt.show()

# Task 6: Heat Map
data = np.array([[30, 40, 50, 20], [25, 35, 45, 15], [40, 50, 60, 30], [35, 45, 55, 25]])
fig, ax = plt.subplots()
cax = ax.imshow(data, cmap='viridis')
ax.set_title("Regional Sales Heat Map")
ax.set_xticks(range(4))
ax.set_xticklabels(['Q1', 'Q2', 'Q3', 'Q4'])
ax.set_yticks(range(4))
ax.set_yticklabels(['North', 'South', 'East', 'West'])
fig.colorbar(cax)
plt.show()

# Task 7: Line Chart
fig, ax = plt.subplots(figsize=(8, 5))
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
revenue = [200, 250, 300, 350, 400]
ax.plot(months, revenue, color='blue', linestyle='dashed')
ax.set_title("Monthly Revenue")
ax.set_xlabel("Months")
ax.set_ylabel("Revenue")
fig.show()
