import matplotlib.pyplot as plt

from die import Die

# Create a die
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# Analyze the results
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results
plt.plot([str(x) for x in range(2, max_result+1)], results)
# hist = pygal.Bar()

# hist.title = "Results of rolling two D6 dice 1000 times"
# hist.x_labels = [str(x) for x in range(2, max_result+1)]
# hist.x_title = "Result"
# hist.y_title = "Frequency of Result"

# hist.add('D6 + D6', frequencies)
# hist.render_to_file('dice_visual.svg')

# ------------

# input_values=[1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.plot(input_values, squares, linewidth=3)

# Set chart title and label axes
plt.title("Results of rolling two D6 dice 1000 times", fontsize=24)
plt.xlabel("Faces", fontsize=14)
plt.ylabel("Results", fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()
