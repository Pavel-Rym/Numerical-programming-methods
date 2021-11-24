import numpy as np
import matplotlib.pyplot as plt

x=np.array([-3, -1, 0, 2])
y=np.array([8, 4 ,-4, -2])

def lagranz(x,y,t):
    result=0
    for j in range(len(y)):
        p1=1; p2=1
        for i in range(len(x)):
            if i==j:
                p1=p1*1; p2=p2*1
            else:
                p1=p1*(t-x[i])
                p2=p2*(x[j]-x[i])
        result=result+y[j]*p1/p2
    return result
xnew=np.linspace(np.min(x),np.max(x))
ynew=[lagranz(x,y,i) for i in xnew]
plt.plot(x,y,'ro',xnew,ynew)
plt.grid()
plt.title('Lagrange')
plt.show()
