
from enum import auto
from tkinter import Tk

from interfaz import Interfaz

from auto import Auto
from autoLogan import AutoLogan

import xml.etree.ElementTree as ET
from carpeta import ArbolDeAutos

def parsearXML():
    mytree=ET.parse('trabajocompi.xml')
    myroot=mytree.getroot()
    return myroot


def extraerDelXMl(x,y):
    return parsearXML()[x][y].text
    
        


       
             

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
        
    
def  mostrarArbol(arbolAutos,autos):
 
    
    print(type(autos[2]))
    for x in range(0,len(autos)):
        arbolAutos.insertarNombreSubCarpeta(autos[x].getNombre())
        arbolAutos.insertarMarcaDeAuto(autos[x].getMarca())
        arbolAutos.insertarAño(autos[x].getAño())
        arbolAutos.insertarTipoDETrasmicion(autos[x].getTransmision())
        
        if(isinstance(autos[x], AutoLogan)):
            arbolAutos.insertarModoDeManejo(autos[x].getModoDeManejo())

    arbolAutos.mostrarArbol()


   # ventana.mostrarArbol(autos[0].getNombre(),autos[0].getMarca(),autos[0].getAño(),autos[0].getTransmision())
    #ventana.mostrarArbol(autos[1].getNombre(),autos[1].getMarca(),autos[1].getAño(),autos[1].getTransmision())

   

class main:
    ventanaPrincipal=Tk()

    #parser=Interfaz(ventanaPrincipal)
    ##crearAutoPruebaBorrarSiSaleMal()
    autos=crearAuto()
    
    
    #--------------------
   #arbolAutos=ArbolDeAutos(ventanaPrincipal)

    arbolAutos=ArbolDeAutos(ventanaPrincipal)
   
    mostrarArbol(arbolAutos,autos)
    
    #app.mainloop()
    
    #----------------n
    #mostrarAutos(autos)
    

    ventanaPrincipal.mainloop()



