from snmp_helper import snmp_get_oid,snmp_extract
COMMUNITY_STRING = 'xxxxxxx'
SNMP_PORT = [7xxx, 8xxx]
IP = 'xx.xxx.xx.xxx'

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
