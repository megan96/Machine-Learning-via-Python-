import matplotlib.pyplot as plt
x = [1,2,3]
y = [3,4,5]
plt.plot(x,y,color ='red',linestyle='dashed',linewidth= 3,marker = 'o' ,markerfacecolor = 'blue',markersize = 12)
plt.ylim(1,7)
plt.xlim(1,7)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title("My Second graph")
plt.show()

