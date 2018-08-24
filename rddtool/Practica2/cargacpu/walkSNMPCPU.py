
from pysnmp.hlapi import *

def consultawalkSNMP(comunidad,host,oid):
    resultado=""
    for (errorIndication,
         errorStatus,
         errorIndex,
         varBinds) in nextCmd(SnmpEngine(),
                              CommunityData(comunidad),
                              UdpTransportTarget((host, 161)),
                              ContextData(),
                              ObjectType(ObjectIdentity(oid)),
                              lexicographicMode=False):

        if errorIndication:
            print(errorIndication)
            break
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            break
        else:
            for varBind in varBinds:
                varB = (' = '.join([x.prettyPrint() for x in varBind]))
                resultado = resultado+varB.split()[2]
                resultado=resultado+": "
    return resultado[0:len(resultado)-2]

def numVar(comunidad,host,oid):
    resultado=0
    for (errorIndication,
         errorStatus,
         errorIndex,
         varBinds) in nextCmd(SnmpEngine(),
                              CommunityData(comunidad),
                              UdpTransportTarget((host, 161)),
                              ContextData(),
                              ObjectType(ObjectIdentity(oid)),
                              lexicographicMode=False):

        if errorIndication:
            print(errorIndication)
            break
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            break
        else:
            for varBind in varBinds:
                resultado+=1
    return resultado