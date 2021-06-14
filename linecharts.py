from matplotlib import pyplot as plt

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

# We can make multiple calls to plt.plot
# to show multiple series on the same chart
plt.plot(xs, variance,    'g-', label='Variance') #Green solid line
plt.plot(xs, bias_squared,   'r-.', label='Bias^2') #Red Dashed Line
plt.plot (xs, total_error,    'b:', label='Total Error') # Blue dotted line

# Because ve have assigned variables to each series
# we can get a legend for free (loc=9 means "top center")

plt.legend(loc=9)
plt.xlabel("Model Complexity")
plt.xticks([])
plt.title("The Bias-Variance Tradeoff")
plt.show()