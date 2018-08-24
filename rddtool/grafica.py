import sys
import rrdtool
import time

tiempo_actual = int(time.time())
tiempo_final = tiempo_actual -3000
tiempo_inicial = tiempo_final

def graficaVel(ip):


    ret = rrdtool.graph(ip+"_vel.png",
                        "--start", str(tiempo_inicial),
                        #                    "--end","N",
                        "--vertical-label=Bytes/s",
                        "DEF:inoctets="+ip+".rrd:inoctets:AVERAGE",
                        "DEF:outoctets="+ip+".rrd:outoctets:AVERAGE",
                        "AREA:inoctets#00FF00:In traffic",
                        "LINE1:outoctets#0000FF:Out traffic\r")

    return ret



def graficaIpRequest(ip):

    ret = rrdtool.graph(ip+"_IpRequest.png" ,
                        "--start", str(tiempo_inicial),
                        #                    "--end","N",
                        "--vertical-label=Bytes/s",
                        "DEF:ipInRequest="+ip+".rrd:ipInRequest:AVERAGE",
                        "DEF:ipOutRequest="+ip+".rrd:ipOutRequest:AVERAGE",
                        "AREA:ipInRequest#00FF00:In traffic",
                        "LINE1:ipOutRequest#0000FF:Out traffic\r")

    return ret


def graficaSnmpPkts(ip):

    ret = rrdtool.graph( ip+"_snmpInPkts.png" ,
                        "--start", str(tiempo_inicial),
                        #                    "--end","N",
                        "--vertical-label=Bytes/s",
                        "DEF:snmpInPkts="+ip+".rrd:snmpInPkts:AVERAGE",
                        "DEF:snmpOutPkts="+ip+".rrd:snmpOutPkts:AVERAGE",
                        "AREA:snmpInPkts#00FF00:In traffic",
                        "LINE1:snmpOutPkts#0000FF:Out traffic\r")

    return ret



def graficaSnmpResponse(ip):

    ret = rrdtool.graph( ip+"_snmpResponse.png",
                        "--start", str(tiempo_inicial) ,
                        #                    "--end","N",
                        "--vertical-label=Bytes/s",
                        "DEF:snmpInGetResponse="+ip+".rrd:snmpInGetResponse:AVERAGE",
                        "DEF:snmpOutGetResponse="+ip+".rrd:snmpOutGetResponse:AVERAGE",
                        "AREA:snmpInGetResponse#00FF00:In traffic",
                        "LINE1:snmpOutGetResponse#0000FF:Out traffic\r")

    return ret


def graficaUdpErrors(ip):


    ret = rrdtool.graph( ip+"_udpInErrors.png" ,
                        "--start", str(tiempo_inicial),
                        #                    "--end","N",
                        "--vertical-label=Bytes/s",
                        "DEF:udpInErrors="+ip+".rrd:udpInErrors:AVERAGE",
                        "LINE1:udpInErrors#0000FF:Out traffic\r")

    return ret

"""while 1:
    ip = 'localhost'
    graficaVel(ip)"""