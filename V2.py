import matplotlib.pyplot as plt

# Input values of X and Y from the console
x_values = input("Enter the values of X separated by commas: ").split(',')
y_values = input("Enter the values of Y separated by commas: ").split(',')

# Convert string values to numbers
x_values = [float(x) for x in x_values]
y_values = [float(y) for y in y_values]

# Plot the graph
plt.plot(x_values, y_values)

# Add title and axis labels
plt.title('Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the graph
plt.show()
