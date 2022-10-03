# 1. Import the requests library
import requests
import xml.etree.ElementTree as ET


URL = "https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-17T00:00:00Z+TO+2021-01-19T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100"

# 2. download the data behind the URL
response = requests.get(URL)


myroot = ET.fromstring(response.content)

print("tag ",myroot.tag)


print('========== child and attrib===========')
for child in myroot:
    print(child.tag, child.attrib)

print()

print("========== Inside element ===============")
for x in myroot.iter('doc'):
    print(x, x.tag, x.attrib, x.text)    

print("========== doc element ===============")
for doc in myroot.findall('doc'):   
    print(doc.find('download_link'))

tree = ET. parse("steeleye.xml")
root = tree. getroot()
x = root. findall("doc")
for value in x:
    print(x. text)
 



    
