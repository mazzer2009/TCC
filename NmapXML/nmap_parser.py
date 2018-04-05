# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET

def printJson(arquivo):
	tree = ET.parse(arquivo)
	root = tree.getroot()
	ipv4 = None
	mac = None
	portId = None
	portService = None
	portState = None
	os = None
	osAcc = None


	#hosts = root.findall('host')
	for results in root.iterfind('host'):
		for address in results.findall('address'):
				if(address.get('addrtype')=="ipv4"):
					ipv4=address.get('addr')
					print(ipv4)
				else:
					mac = address.get('addr')
					print(mac)

		if(results.find('./ports/port')):
			for ports in results.findall('./ports/port'):
				portId = ports.get('portid')
				portState = ports.find('./state').get('state')
				portService = ports.find('./service').get('name')
				print(portState)

		if(results.find('.os/osmatch')):
			os = results.find('.os/osmatch').get('name')
			osAcc = results.find('.os/osmatch').get('accuracy')
			print(os + " " + osAcc + "%")


	#print(root.child)

printJson("/home/emanuel/nmap_file2.xml")