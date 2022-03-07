
from tkinter import Tk

from interfaz import Interfaz

from auto import Auto
from autoLogan import AutoLogan

import xml.etree.ElementTree as ET
from carpeta import Concesionario

def parsearXML():
    mytree=ET.parse('trabajocompi.xml')
    myroot=mytree.getroot()
    return myroot


def extraerDelXMl(x,y):
    return parsearXML()[x][y].text
    
        
def crearAutoPruebaBorrarSiSaleMal():
    array1=[]
    array2=[]
    index2=0
    index=0
    for x in [0,1,2]:
        
        for y in [0,1,2,3,4]:
            array1.insert(index,extraerDelXMl(x,y)) 
            index+=1

    for yy in [1,2,3]:
        for zz in [1,2,3,4,5]:            
            array2.insert(index2,array1)
            
    print('->>>><',array2[1])    

    

       
             

def crearAuto():
    array=[]
    arrayDeObjetos=[]
    index=0
    for x in [0,1,2]:
        for y in [0,1,2,3,4]:
            array.insert(index,extraerDelXMl(x,y))  
            if(x==2 and y==0):
                array.insert(index,extraerDelXMl(x,y)) 
            index+=1
         
    rio=Auto(array[0],array[1],array[2],array[3],array[4])
    sandero=Auto(array[5],array[6],array[7],array[8],array[9])
    logan=AutoLogan('logan','renault',2022,'automatica','blue','sport')
    
    

    arrayDeObjetos.insert(0,rio)
    arrayDeObjetos.insert(1,sandero)
    arrayDeObjetos.insert(2,logan)
    
    

    return arrayDeObjetos
    
    
def  mostrarAutos(autos):
   
    for x in autos:
        print(x.toString())
        
    

class main:
    ventanaPrincipal=Tk()
    parser=Interfaz(ventanaPrincipal)
    ##crearAutoPruebaBorrarSiSaleMal()
    autos=crearAuto()
    
    #--------------------
    
    app = Concesionario(ventanaPrincipal)
    #app.mainloop()
    
    #----------------
    mostrarAutos(autos)
    

    ventanaPrincipal.mainloop()



