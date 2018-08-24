import rrdtool

def crearBD(ip):
    ret = rrdtool.create(ip + '.rrd',
                         "--start", 'N',
                         "--step", '60',
                         "DS:inoctets:COUNTER:600:U:U",  #octetos de entrada intrfaz
                         "DS:outoctets:COUNTER:600:U:U",  # octetos de salida  interfaz
                         "DS:ipInRequest:COUNTER:600:U:U",  # octetos de salida  interfaz
                         "DS:ipOutRequest:COUNTER:600:U:U",  # octetos de salida  interfaz
                         "DS:snmpInPkts:COUNTER:600:U:U",  # octetos de salida  interfaz
                         "DS:snmpOutPkts:COUNTER:600:U:U",  # octetos de salida  interfaz
                         "DS:snmpInGetResponse:COUNTER:600:U:U",  # octetos de salida  interfaz
                         "DS:snmpOutGetResponse:COUNTER:600:U:U",  # octetos de salida  interfaz
                         "DS:udpInErrors:COUNTER:600:U:U",  # octetos de salida  interfaz
                         "RRA:AVERAGE:0.5:6:600",
                         "RRA:AVERAGE:0.5:6:600",
                         "RRA:AVERAGE:0.5:6:600",
                         "RRA:AVERAGE:0.5:6:600",
                         "RRA:AVERAGE:0.5:6:600",
                         "RRA:AVERAGE:0.5:6:600",
                         "RRA:AVERAGE:0.5:6:600",
                         "RRA:AVERAGE:0.5:6:600",
                         "RRA:AVERAGE:0.5:6:600"

                         #"DS:inoctets:COUNTER:600:U:U",
                         #"DS:outoctets:COUNTER:600:U:U",
                         #"RRA:AVERAGE:0.5:6:700",
                         # "RRA:AVERAGE:0.5:1:600"

                         )
   # return ret
