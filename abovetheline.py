# Imports
import matplotlib.pyplot as plt
import random
import numpy as np
import pandas as pd

# Inputs
m = [float(input('Slope?'))]*4
b = [float(input ('Y Intercept?'))]*4

# Set up rotations and test points
rotations = range(4)
testpoints = []
for i in range(100):
  testpoints.append([random.randint(-50,51), random.randint(-50,51)])

# Create points series and dataframe for results
points = pd.Series( data=testpoints )
results = pd.DataFrame( columns=rotations )

# Create Rotated Slopes and Intercepts
for rotation in range(4):
  if rotation == 1:
    m[rotation] = -1/m[0]
    b[rotation] = -b[0]/m[0]
  elif rotation == 2:
    b[rotation] = -b[0]
  elif rotation == 3:
    m[rotation] = -1/m[0]
    b[rotation] = b[0]/m[0]
    
# Is Point Above Line?
def isAbove(point,m,b):
  if (point[1] > m * point[0] + b):
    return True

# Perform Each Rotation
for i in rotations: 
  results[i] = points.apply( isAbove, args=(m[i],b[i]) ) 

# print(df)
print(results)


## Optional Plotting To Visualize

# Create Subplot
def subPlot(plot,m,b,testpoints,rotation):
  plot.subplot(2, 2, rotation + 1)
  xl = np.linspace(-200,200,100)
  yl = m*xl+b
  plot.plot(xl, yl, '-r', label='y='+str(m)+'x+'+str(b))
  plot.title('Graph of ' + str(rotation) + ' Rotation')
  plot.legend(loc='upper left')
  plot.axis([-50, 50, -50, 50])
  plot.grid()
  for point in testpoints:
    if ( point[1] > point[0] * m + b ):
      plot.plot(point[0],point[1],'ro', color="green")
    else:
      plot.plot(point[0],point[1],'ro', color="red")

# Plot Rotations
for rotation in range(4):
  subPlot(plt,m[rotation],b[rotation],testpoints,rotation)
plt.show()