from snmp_helper import snmp_get_oid,snmp_extract
COMMUNITY_STRING = 'galileo'
SNMP_PORT = [7961, 8061]
SNMP_PORT1 = 8061
IP = '50.242.94.227'

a_device = (IP, COMMUNITY_STRING, SNMP_PORT[0])
b_device = (IP, COMMUNITY_STRING, SNMP_PORT[1])
device = [(IP, COMMUNITY_STRING, SNMP_PORT[0]),(IP, COMMUNITY_STRING, SNMP_PORT[1])]

OID = ['1.3.6.1.2.1.1.5.0', '1.3.6.1.2.1.1.1.0']

i = 0
for i in range(i, len(OID)):
    snmp_sys_data = snmp_get_oid(device[i], oid=OID[0])
    snmp_desc_data = snmp_get_oid(device[i], oid=OID[1])
    output_sys = snmp_extract(snmp_sys_data)
    output_desc = snmp_extract(snmp_desc_data)
    print output_sys 
    print output_desc
