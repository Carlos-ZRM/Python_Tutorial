
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

class Plot_Time_Series:
    def read_file(self, path):
        f = open(path, 'r')
        str = f.read();
        f.close()
        return str

    def f(self, t):
        return np.exp(-t) * np.cos(2*np.pi*t)

    def make_graf_str(self, string, spl, dt):
        str = file_r().split( spl )
        s1_aux = []
        for i in range(len(str)):
            s1_aux.append( int(str[i]))
        t = np.arange(0,len(str)-1,dt)
        x = np.array(s1_aux)
        return x , y
    def plot():
        fig, (ax1) = plt.subplots()
        ax1.plot(t, np.array(s1))
        plt.show()
