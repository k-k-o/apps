#!/usr/bin/python
# -*- coding: utf-8 -*-

import libxml2dom
import urllib
import time
import sys
import datetime

def collect_text(node):
    s = ""
    for child_node in node.childNodes:
        if child_node.nodeType == child_node.TEXT_NODE:
            s += child_node.nodeValue.encode('utf-8').strip()+"\n"
        else:
            s += collect_text(child_node)
    return s

def ref_date(date):
	ind = date.index("cja ")
	date = date[ind+4:len(date)]
	"Zamienia date, np. 2007-10-20 22:21, na odpowiednią: Sat, 20 Oct 2007 22:21:00 +0200"
	data = datetime.datetime(*time.strptime(date, "%d-%m-%Y %H:%M\n")[0:5])
	rob = data.strftime("%a, %d %b %Y %H:%M:%S %Z")
	return rob

def get_items(adress, filename):
   #urllib.urlretrieve(adress, 'foto-kko.jpg')
   #urllib.urlretrieve(adress, 'E25749_800.jpg')
   urllib.urlretrieve(adress, filename)
   #urllib.urlretrieve(adress, 'plik-kko.html')
   #s = f.read()

   outstr=""
   #doc = libxml2dom.parseString(s, html=1)
   #div_elements = doc.getElementsByTagName("div")

   titlelink = ""
   indexlink = ""
   nowindex = 1

   index = ""
   title = ""
   teaser = ""
   date = ""
   author = ""
   return outstr

# print a_elements

#adress = sys.argv[1]
#adress = "http://www.tobar.co.uk/media/catalog/product/E25749_800.jpg"
adressy = ("http://www.tobar.co.uk/media/catalog/product/E25875_800.jpg", "http://www.tobar.co.uk/media/catalog/product/E25648_800.jpg")
pliki = ("E25875_800.jpg", "E25648_800.jpg")
outstr = ''
error = 'blad'
try:
    for i in [0,1]:
        rob1=get_items(adressy[i], pliki[i])
    #outstr+=rob1
except:
  error = 'blad2'


#print outstr
