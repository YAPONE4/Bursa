import xml.etree.cElementTree as ET
import urllib.request as urllib2
import shutil
import datetime
import xml.dom.minidom

def get_file(date):
    get = urllib2.Request('http://www.cbr.ru/scripts/XML_daily.asp?date_req={}'.format(date))
    getf = urllib2.urlopen(get)
    file = open('data.xml', 'wb')
    shutil.copyfileobj(getf, file)

def xml_fill_comboblox_names(file):
    dom = xml.dom.minidom.parse(file)
    dom.normalize()
    nodeArray = dom.getElementsByTagName('Name')
    info = ['Российский рубль']
    for node in nodeArray:
        childList = node.childNodes
        info.append(childList[0].nodeValue)
    return info

if __name__ == "__main__":
    get_file('08/05/2021')
    with open('data.xml', 'rb') as file:
        xml_fill_comboblox_names(file)