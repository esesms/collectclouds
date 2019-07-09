import matplotlib.pyplot as plt

# Data to plot
labels = 'sweet', ' candy ', ' silk ', 'strawberries ', 'marshmallows', 'cheese', 'vanilla', 'tart'
sizes = [13, 12, 5, 3, 3, 3, 2, 1]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'purple', 'magenta', 'blue']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=False, startangle=140)

plt.axis('equal')
plt.show()