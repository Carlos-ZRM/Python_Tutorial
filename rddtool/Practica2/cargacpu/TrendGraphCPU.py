import sys
import rrdtool
import time
from walkSNMP import numVar
definitions=[]
lines=[]
colors=['FF0000','00FF00','0000FF','000000','00FFFF','FF00FF','FFFF00']
var=numVar('comunidadSNMP','localhost','1.3.6.1.2.1.25.3.3.1.2')
for i in range(0,var):
    definitions.append('DEF:carga'+str(i)+'=trend2.rrd:CPUload'+str(i)+':AVERAGE')
    lines.append('LINE2:carga'+str(i)+'#'+colors[i]+':CPU'+str(i)+' load')
while 1:
    ret = rrdtool.graph( "trend2.png",
                     "--start",'1525039690',
                     "--vertical-label=Carga CPU",
                     "--title=Uso de CPU",
                     "--color", "ARROW#009900",
                     '--vertical-label', "Uso de CPU (%)",
                     '--lower-limit', '0',
                     '--upper-limit', '100',
                     definitions,
                     lines,
                     "LINE1:30")
    time.sleep(4)
