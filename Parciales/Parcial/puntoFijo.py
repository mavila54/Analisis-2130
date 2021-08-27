import numpy as np

def fx(x):
    return 2+np.sin(x)-x

def gx(x):
    return 2+np.sin(x)

Tolerancia = 10E-5
xi=0
Error=np.abs(gx(xi)-xi)
i=0
while (Error>Tolerancia and i<=100):
    print(i,'  Raiz=',"{0:.5f}".format(xi),'  f(xi)',"{0:.5f}".format(fx(xi)),'  g(xi)',"{0:.5f}".format(gx(xi)),'  Error=',"{0:.5f}".format(Error))
    if i>0:
        Error=np.abs(gx(xi)-xi)
    xi=gx(xi)
    i = i+1