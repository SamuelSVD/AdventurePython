from classes import *

def loadEnvironment(x,y):
    f = open('Map/%d_%d.SAM' % (x,y),'r').read()
    #print f

    f = f.split('\n')
    #print f
    
    size = f[0].split()
    f = f[1:]
    for i in range(len(f)):
        f[i] = f[i].split()

    for i in range(len(size)):
        size[i] = int(size[i])
    
    E = Environment(size[0],size[1])
    for i in range(len(f)):
        for j in range(len(f[i])):
            E.setComponent(i,j,EnvironmentComponent(i,j,int(f[j][i])))
    
    return E    
