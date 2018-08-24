import time
import rrdtool
from uno.getSNMP import consultaSNMP
from uno.crearBD import crearBD
import threading

class HiloObj(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name,
                         daemon=daemon)
        self.comunidad = args[0]
        self.ip = args[1]
        crearBD(self.ip)
        self.condicion = 1

    def snmpOIDS(self):

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
        oid_snmpInGetResponse = '1.3.6.1.2.1.7.1.0'
        total_snmpOutGetResponse= 0
        oid_snmpOutGetResponse = '1.3.6.1.2.1.7.4.0'

        total_udpErrors = 0
        oid_udpErrors = '1.3.6.1.2.1.7.3.0'




        total_input_traffic = int(consultaSNMP(self.comunidad, self.ip, oid_input_traffic ))
        total_output_traffic = int(consultaSNMP(self.comunidad, self.ip , oid_output_traffic ))
        total_ipInRequest   = int(consultaSNMP(self.comunidad, self.ip , oid_ipInRequest ))
        total_ipOutRequest = int(consultaSNMP(self.comunidad, self.ip , oid_ipOutRequest ))
        total_snmpInPkts    = int(consultaSNMP(self.comunidad, self.ip , oid_snmpInPkts ))
        total_snmpOutPkts   = int(consultaSNMP(self.comunidad, self.ip , oid_snmpOutPkts ))
        total_snmpInGetResponse = int(consultaSNMP(self.comunidad, self.ip , oid_snmpInGetResponse ))
        total_snmpOutGetResponse  = int(consultaSNMP(self.comunidad, self.ip , oid_snmpOutGetResponse ))
        total_udpErrors = int(consultaSNMP(self.comunidad, self.ip , oid_udpErrors ))


        valor = "N:{0}:{1}:{2}:{3}:{4}:{5}:{6}:{7}:{8}".format(str(total_input_traffic), str(total_output_traffic),
                                                               str(total_ipInRequest), str(total_ipOutRequest),
                                                               str(total_snmpInPkts), str(total_snmpOutPkts),
                                                               str(total_snmpInGetResponse), str(total_snmpOutGetResponse),
                                                               str(total_udpErrors))
        print(self.ip+' ? '+valor)
        rrdtool.update(self.ip + '.rrd', valor)
        rrdtool.dump(self.ip + '.rrd', self.ip + '.xml')


    def run(self):
       while 1:
         if self.condicion:
            self.snmpOIDS()
       else:
            print('muerto a la verga')


    def getIp(self):
          return self.ip
    def exit(self):
        self.condicion = 0


"""
ip2 = '10.0.0.15'
ip = 'localhost'

comunidad = 'comunidadCarlos'



hilo = HiloObj(args=(comunidad, ip ), daemon=False)
hilo2 = HiloObj(args=(comunidad, ip2 ), daemon=False)


lista = {}
lista[hilo.getIp()] = hilo
lista[hilo2.getIp()] = hilo2


print(len(lista))


hilo.start()
hilo2.start()



#hilo.exit()


del lista[hilo.getIp()]

print(len(lista))



"""

