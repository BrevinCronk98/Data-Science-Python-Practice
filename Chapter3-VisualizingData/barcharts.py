from matplotlib import pyplot as plt
from collections import Counter
from numpy.lib.histograms import histogram

#----------------Movie Bar Chart---------------------------#

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gahndi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# plot bars with left x-coordinates [0, 1, 2, 3, 4], heights [num_oscars]
plt.bar(range(len(movies)), num_oscars)

plt.title("My Favorite Movies")  # Add a title
plt.ylabel("# of Academy Awards") # Label the Y-axis

#label x-axis with movie names at bar centers
plt.xticks(range(len(movies)), movies)

plt.show()
#-------------------------------------------------------#

#---------------------Grades Bar Graph------------------#
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

#Bucket grades by decile, but put 100 in with the 90s
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()], # Shifts bars right by a value of 5
histogram.values(),                        # Gives each bar its correct height
10,                                        # Give each bar a width of 10
edgecolor=(0, 0, 0))                       # Black edges for each bar

plt.axis([-5, 105, 0, 5])                  # Gives the x-axis range of -5 to 105
                                           # The second pair of numbers is the y-axis range, in this case, 0, to 5

plt.xticks([10 * i for i in range(11)])    #x axis labels at increments of 10
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distibution of Exam 1 Grades")
plt.show()
#---------------------------------------------------#

