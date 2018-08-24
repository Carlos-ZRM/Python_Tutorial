import time
import rrdtool
from walkSNMP import consultawalkSNMP,numVar
print numVar('comunidadSNMP','localhost',
                     '1.3.6.1.2.1.25.3.3.1.2')
while 1:
    carga_CPU=str(consultawalkSNMP('comunidadSNMP','localhost',
                     '1.3.6.1.2.1.25.3.3.1.2'))
    valor = "N:" + carga_CPU
    print valor
    rrdtool.update('trend2.rrd', valor)
    rrdtool.dump('trend2.rrd','trend2.xml')
    time.sleep(1)

if ret:
    print rrdtool.error()
    time.sleep(300)
