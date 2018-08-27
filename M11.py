import matplotlib.pyplot as plot

import csv
x = []
y = []
with open('txt.csv','r') as cfile:
 p = csv.reader(cfile)
 for col in p:
   x.append(col[0])
   y.append(col[1])
plot.plot(x,y,label ='File')
plot.xlabel('x')
plot.ylabel('y')
plot.title('Test Graph')
plot.legend()
plot.show()
