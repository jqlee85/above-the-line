# Imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Inputs
m = [float(input('Slope?'))]*4
b = [float(input ('Y Intercept?'))]*4

# Set up rotations and test points
rotations = range(4)
testpoints = [[0,0],[1,9],[1,-9],[-1,9],[-1,-9],[10,5],[2,-5],[-3,4],[-3,-4],[8,2],[-8,2],[2,-8],[2,8],[10,6],[1,3],[-7,-1],[-10,-4],[-1,-1],[-1,1]]

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
    
# Create DataFrame
# data = {'points':testpoints}
points = pd.Series( data=testpoints )
df2 = pd.DataFrame( columns=rotations )
print(df2)
def isAbove(point,m,b):
  if (point[1] > m * point[0] + b):
    return True
  
for i in rotations: 
  df2[i] = points.apply( isAbove, args=(m[i],b[i]) ) 

# print(df)
print(df2)


#### Plotting

# Create Subplot
def subPlot(plot,m,b,testpoints,rotation):
  plot.subplot(2, 2, rotation + 1)
  xl = np.linspace(-200,200,100)
  yl = m*xl+b
  plot.plot(xl, yl, '-r', label='y='+str(m)+'x+'+str(b))
  plot.title('Graph of ' + str(rotation) + ' Rotation')
  plot.legend(loc='upper left')
  plot.axis([-20, 20, -20, 20])
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