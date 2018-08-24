import rrdtool
from walkSNMP import numVar

var=numVar('comunidadSNMP','localhost','1.3.6.1.2.1.25.3.3.1.2')
data=[]
for i in range(0,var):
    data.append('DS:CPUload'+str(i)+':GAUGE:600:U:U')
ret = rrdtool.create("trend2.rrd",
                     "--start",'N',
                     "--step",'10',
                     data,
                     "RRA:AVERAGE:0.5:1:24")
if ret:
    print rrdtool.error()
