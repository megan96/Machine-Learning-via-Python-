import matplotlib.pyplot as plt
x = [1,2,3]
y = [3,8,5]
plt.plot(x,y,label='line1')
x1 = [3,8,5]
y1 = [1,2,3]
plt.plot(x1,y1,label='line2')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title("My Second graph")
plt.legend()
plt.show()

