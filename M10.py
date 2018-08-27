import numpy as np
import matplotlib.pyplot as plot

 # Get x values of the sine wave

x  = np.arange(0, 2*(np.pi), 0.1);
'''first parameter is starting point 2nd parameter is unit circle which displays with time and third parameter is sampling frequency'''
 

# Amplitude of the sine wave is sine of a variable like time

y1 = np.sin(x)

y2 = np.cos(x)

# Plot a sine wave using time and amplitude obtained for the sine wave

plot.plot(x, y1,label='Sin')
plot.plot(x,y2,label='Cos')
 


 

#plot.grid(True, which='both')

 

#plot.axhline(y=0, color='k')

 

plot.legend()

 

# Display the sine wave

plot.show()
