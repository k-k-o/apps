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

def get_items(filename):
   adress = "http://www.tobar.co.uk/media/catalog/product/"+filename
   urllib.urlretrieve(adress, filename)
   #urllib.urlretrieve(adress, 'plik-kko.html')
   #s = f.read()

   outstr=""

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
#adressy = ("http://www.tobar.co.uk/media/catalog/product/E25875_800.jpg", "http://www.tobar.co.uk/media/catalog/product/E25648_800.jpg")
#pliki = ("E19208_800.jpg","E7700_800.jpg","E4930_800.jpg","E25903_800.jpg","E15500_800.jpg","E24838_800.jpg","E24720_800.jpg","E24701_800.jpg","E25765_800.jpg","E25796_800.jpg","E25561_800.jpg","E25788_800.jpg","E25647_800.jpg","E25781_800.jpg","E25640_800.jpg","E25785_800.jpg","E25099_800.jpg","E25721_800.jpg","E25760_800.jpg","E25878_800.jpg","E26453_800.jpg","E25745_800.jpg","E25767_800.jpg","E25749_800.jpg","E25950_800.jpg","E25634_800.jpg","E25650_800.jpg","E24834_800.jpg","E25710_800.jpg","E25556_800.jpg","E25747_800.jpg","E25734_800.jpg","E25724_800.jpg","E26437_800.jpg","E25335_800.jpg","E25589_800.jpg","E24685_800.jpg","E24688_800.jpg","E24686_800.jpg","E24689_800.jpg","E24691_800.jpg","E24418_800.jpg","E26883_800.jpg","E24744_800.jpg","E24739_800.jpg","E24418_800.jpg")
#pliki = ("E14816_800.jpg","E14819_800.jpg","E14756_800.jpg","E15804_800.jpg","E14824_800.jpg","E14942_800.jpg","E14845_800.jpg","E15703_800.jpg","E14938_800.jpg","E15242_800.jpg","E15163_800.jpg","E16270_800.jpg","E20906_800.jpg","E15764_800.jpg")
pliki = ("E15934_800.jpg","E19630_800.jpg","E12781_800.jpg","E12781_800.jpg","E12779_800.jpg","E18753_800.jpg","E15499_800.jpg","E12936_800.jpg","E12935_800.jpg","E26881_800.jpg","E26885_800.jpg","E26884_800.jpg","E26886_800.jpg","E24735_800.jpg","E24738_800.jpg","E24733_800.jpg","E24742_800.jpg","E24740_800.jpg","E24416_800.jpg","E24417_800.jpg","E24415_800.jpg","E24690_800.jpg","E24692_800.jpg","E5717_800.jpg","E13006_800.jpg","E24416_800.jpg","E24415_800.jpg","E24417_800.jpg","E26542_800.jpg","E25761_800.jpg","E25766_800.jpg","E25762_800.jpg","E25763_800.jpg","E26543_800.jpg","E26544_800.jpg","E25797_800.jpg","E25756_800.jpg","E26032_800.jpg","E26451_800.jpg","E25829_800.jpg","E25830_800.jpg","E25823_800.jpg","E25822_800.jpg","E25609_800.jpg","E25889_800.jpg","E25890_800.jpg","E25743_800.jpg","E25740_800.jpg","E25738_800.jpg","E25888_800.jpg","E25737_800.jpg","E25736_800.jpg","E25735_800.jpg","E25746_800.jpg","E25748_800.jpg","E25799_800.jpg","E25825_800.jpg","E25817_800.jpg","E25594_800.jpg","E25593_800.jpg","E25824_800.jpg","E24705_800.jpg","E24704_800.jpg","E24703_800.jpg")
dl = len(pliki)
outstr = ''
error = 'blad'
try:
    for i in range(dl):
        #print i, ' -- ',pliki[i]
        rob1=get_items(pliki[i])
    #outstr+=rob1
except:
  error = 'blad2'


#print outstr
