import time
import rrdtool
from uno.getSNMP import consultaSNMP
from uno.crearBD import crearBD
import threading



def snmpOIDS(comunidad, ip):

    total_input_traffic = 0
    oid_input_traffic = '1.3.6.1.2.1.2.2.1.10.3'
    total_output_traffic = 0
    oid_output_traffic = '1.3.6.1.2.1.2.2.1.16.3'

    total_ipInRequest = 0
    oid_ipInRequest = '1.3.6.1.2.1.4.3.0'
    total_ipOutRequest = 0
    oid_ipOutRequest = '1.3.6.1.2.1.4.10.0'


    total_snmpInPkts = 0
    oid_snmpInPkts = '1.3.6.1.2.1.11.1.0'
    total_snmpOutPkts = 0
    oid_snmpOutPkts = '1.3.6.1.2.1.11.2.0'


    total_snmpInGetResponse = 0
    oid_snmpInGetResponse = '1.3.6.1.2.1.11.18.0'
    total_snmpOutGetResponse= 0
    oid_snmpOutGetResponse = '1.3.6.1.2.1.11.28.0'

    total_udpErrors = 0
    oid_udpErrors = '1.3.6.1.2.1.7.3.0'




    total_input_traffic = int(consultaSNMP(comunidad, ip, oid_input_traffic ))
    total_output_traffic = int(consultaSNMP(comunidad, ip , oid_output_traffic ))
    total_ipInRequest   = int(consultaSNMP(comunidad, ip , oid_ipInRequest ))
    total_ipOutRequest = int(consultaSNMP(comunidad, ip , oid_ipOutRequest ))
    total_snmpInPkts    = int(consultaSNMP(comunidad, ip , oid_snmpInPkts ))
    total_snmpOutPkts   = int(consultaSNMP(comunidad, ip , oid_snmpOutPkts ))
    total_snmpInGetResponse = int(consultaSNMP(comunidad, ip , oid_snmpInGetResponse ))
    total_snmpOutGetResponse  = int(consultaSNMP(comunidad, ip , oid_snmpOutGetResponse ))
    total_udpErrors = int(consultaSNMP(comunidad, ip , oid_udpErrors ))


    valor = "N:{0}:{1}:{2}:{3}:{4}:{5}:{6}:{7}:{8}".format(str(total_input_traffic), str(total_output_traffic),
                                                           str(total_ipInRequest), str(total_ipOutRequest),
                                                           str(total_snmpInPkts), str(total_snmpOutPkts),
                                                           str(total_snmpInGetResponse), str(total_snmpOutGetResponse),
                                                           str(total_udpErrors))
    print(valor)
    rrdtool.update(ip + '.rrd', valor)
    rrdtool.dump(ip + '.rrd', ip + '.xml')


def hiloM(comunidad, ip):
   while 1:
     snmpOIDS(comunidad, ip)



ip2 = '10.100.68.114'
ip = 'localhost'

crearBD(ip)
crearBD(ip2)
comunidad = 'comunidadCarlos'


hilo1 = threading.Thread(target=hiloM, args=(comunidad, ip))
hilo2 = threading.Thread(target=hiloM, args=(comunidad, ip))
hilo1.start()
hilo2.start()




