#histogram for showing distribution
import matplotlib.pyplot as plt
ages = [2,5,70,30,40,50,65,73,85,90,50,45,70,49,68,45,67,21,22,23,24,25]
range = (0,100)
bins = 10
plt.hist(ages,bins,range,color='red',histtype='bar',rwidth = 0.8)
plt.xlabel('Age')
plt.ylabel('No of people')
plt.title("My histogram")
plt.show()

