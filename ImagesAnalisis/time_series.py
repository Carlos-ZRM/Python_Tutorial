
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

class Plot_Time_Series:

    def __init__(self):
        self.__id=0
    def read_file(self, path):
        f = open(path, 'r')
        str = f.read();
        f.close()
        return str

    def f(self, t):
        return np.exp(-t) * np.cos(2*np.pi*t)

    def make_graf_str(self, str, spl):
        str = file_r().split( spl )
        s1_aux = []
        for i in range(len(str)):
            s1_aux.append( int(str[i]))
        #t = np.arange(0,len(str),1)
        y = []
        x = np.array(s1_aux)
        yield x
        yield y
    def make_graf_arr( self, array):
        dt = 1
        y = np.arange(0,len(array), 1)
        x = np.array(array)
        yield x
        yield y

    def plot_Histograma( self, array ):
        x , y = self.make_graf_arr(array)
        fig, (ax1) = plt.subplots()
        ax1.plot( y , x )
        plt.show()
