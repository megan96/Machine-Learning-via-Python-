#Pie Chart for showing distribution
import matplotlib.pyplot as plt
activities = ['music','dance','skiing','eat']
slices = [3,7,8,6]
colors  = ['r','m','g','b']
plt.pie(slices,labels=activities,colors=colors,startangle= 90,shadow=True,explode = (0,0,0,0.1),autopct = '%1.5f')

plt.legend()
plt.show()

