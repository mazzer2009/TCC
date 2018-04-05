# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import json as js
class port:
    def __init__(self):
        self.portId = None
        self.portService = None
        self.portState = None


def extracaoDados(arquivo):
	tree = ET.parse(arquivo)
	root = tree.getroot()
	ipv4 = None
	mac = None
	os = None
	osAcc = None


	#hosts = root.findall('host')
	for results in root.iterfind('host'):
		ports = [port()for i in range(len(results.findall('./ports/port')))]
		for address in results.findall('address'):
				if(address.get('addrtype') == "ipv4"):
					ipv4 = address.get('addr')
				else:
					mac = address.get('addr')

		if(results.find('./ports/port')):
			i = 0
			for portas in results.findall('./ports/port'):
				
				ports[i].portId = portas.get('portid')
				ports[i].portState = portas.find('./state').get('state')
				ports[i].portService = portas.find('./service').get('name')
				i+=1
		if(results.find('.os/osmatch')):
			os = results.find('.os/osmatch').get('name')
			osAcc = results.find('.os/osmatch').get('accuracy')

	printJson(ports, ipv4, mac, os)

def printJson(ports, ipv4, mac, os):
	json=('"MAC":"{0}","ipv4":"{1}","OS":"{2}","ports":'.format(mac,ipv4,os))
	json = json + "{"
	if(len(ports) == 0):
		json = json + "}"
	else:

		for i in range(len(ports)):
			json =(json +'"{0}":"{1}",'.format(ports[i].portId,ports[i].portService))
		json = (json[:-1] + "}")
	json = "{" + json + "}"
	print(json)
	return json


	#print(root.child)

extracaoDados("/home/suporte/Documentos/GitHub/TCC/NmapXML/nmap_file2.xml")