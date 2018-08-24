import time
import rrdtool
from getSNMP import consultaSNMP

total_input_traffic = 0
total_output_traffic = 0


while 1:
    total_input_traffic = int(consultaSNMP('comunidadSNMP','localhost','1.3.6.1.2.1.2.2.1.10.3'))
    total_output_traffic = int(consultaSNMP('comunidadSNMP','localhost','1.3.6.1.2.1.2.2.1.16.3'))

    valor = str(rrdtool.last("netP.rrd")+100)+":" + str(total_input_traffic) + ':' + str(total_output_traffic)
    print valor
    ret = rrdtool.update('netP.rrd', valor)
    rrdtool.dump('netP.rrd','netP.xml')

    ret = rrdtool.graph("netP.png",
                        "--start", '1524174069',
                        "--end",str(rrdtool.last('netP.rrd')),
                        "--vertical-label=Bytes/s",
                        "DEF:obs=netP.rrd:inoctets:AVERAGE",
                        "DEF:outoctets=netP.rrd:outoctets:AVERAGE",
                        "DEF:pred=netP.rrd:inoctets:HWPREDICT",
                        "DEF:dev=netP.rrd:inoctets:DEVPREDICT",
                     #"RRA:DEVSEASONAL:1d:0.1:2",
                     #"RRA:DEVPREDICT:5d:5",
                     #"RRA:FAILURES:1d:7:9:5""
                        "CDEF:scaledobs=obs,8,*",
                        "CDEF:upper=pred,dev,2,*,+",
                        "CDEF:lower=pred,dev,2,*,-",
                        "CDEF:scaledupper=upper,8,*",
                        "CDEF:scaledlower=lower,8,*",
                        "LINE1:scaledobs#00FF00:In traffic",
                        "LINE1:outoctets#0000FF:Out traffic",
                        "LINE1:scaledupper#ff0000:Upper Bound Average bits out",
                        "LINE1:scaledlower#ff0000:Lower Bound Average bits out")

    time.sleep(1)

if ret:
    print rrdtool.error()
    time.sleep(300)
