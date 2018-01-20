import numpy as np
import matplotlib.pyplot as pl
data1 = np.loadtxt("testdata.csv", delimiter=",", skiprows=1)
#this is a comment
print("Hello!")
pl.figure(1)
pl.plot(data1[:,0],data1[:,1], "r--*")
pl.xlabel("time:")
pl.ylabel("${}^0C$")
pl.legend(["temp"])
xx = np.arange(0,100,0.5)
yy= np.sin(xx/100*np.pi)*20+10
pl.figure(2)
pl.plot(xx,yy,"g")
pl.legend(["wave"])
pl.xlim(xmax=150,xmin=0)
pl.title("My graph")
pl.show()
