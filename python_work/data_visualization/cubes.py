import matplotlib.pyplot as plt

# values = list(range(1, 6))
values = list(range(1, 5001))
cubed_values = [x**3 for x in values]

plt.scatter(values, cubed_values, c=cubed_values, cmap=plt.cm.Reds, edgecolor='none', s=40)

# Set chart title and label axes
plt.title("Cubed Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
# plt.axis([0, 1100, 0, 1100000])

plt.show()