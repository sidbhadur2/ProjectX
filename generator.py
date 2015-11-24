import urllib2
import musixmatch
from urllib2 import Request, urlopen, URLError
import  xml.etree
import lxml
from lxml import objectify
import re

for i in range(90):
	print "with open" + "(" "\"" + "l" + str(11+i) +".txt" + "\"" + ",'r')" + "as f:"
	print "	split=" + "f.read().strip().splitlines()"
	print "	f.close()"
	print ("	for num,line in enumerate(split,1):")
	print ("		a = re.split(' ' ,line)")
	print ("		print ('tweet' + str(num) + ' = ' + str(a))")
	print '\n'
