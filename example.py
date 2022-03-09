#from xml.dom.minidom import Element
import xml.etree.ElementTree as ET
#from tkinter import Tk
mytree=ET.parse('trabajocompi.xml')
myroot=mytree.getroot()
# self
#print('[[[[[[[[[[[[[[{',myroot[0][0].tag,']]]]]]]]]]]]]]]]]')

for x in [0,1,2]:
        for y in [0,1,2,3]:
            print(x,'YYYYY',y)

#for x in myroot[0]:
 #   print (x.text)
 #   print(x.tag,x.attrib)


 