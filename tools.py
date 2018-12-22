#!/usr/bin/python

from xml.etree import ElementTree
from datetime import datetime


# UNIXITEM to Readable time
def time_from_epoch(string):
	timefromepoch = datetime.fromtimestamp(float(string))
	return timefromepoch

# KByte from Byte
def kbyte_from_byte(string):
	result = float(string)/1024
        s = str(round(result,2)) + " KByte"
	return s         

# MByte from Byte
def mbyte_from_byte(string):
	result = float(string)/1024/1024
        s = str(round(result,4)) + " MByte"
	return s         

# Extract attribuite value from XML 
def dump_xml(xml,attribute):
	root =  ElementTree.fromstring(xml)
	tree = ElementTree.ElementTree(root)
	for i in root:
		print(i.get(attribute))

# How to use
# <element attribuite="value">element value</element>
samplexml = '''<?xml version="1.0" encoding="ISO-8859-1"?>
		<stat directory="/mydir">
			<file type="file" name="test1.log.gz" size="1292464" />
			<file type="file" name="test2.log.gz" size="1292464" />
		</stat>'''
#
# dump_xml(samplexml,'name')

