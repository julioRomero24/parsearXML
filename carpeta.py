
from asyncio.windows_events import NULL

import tkinter as tk
from tkinter import ttk

class ArbolDeAutos(ttk.Frame):
    
    def __init__(self, ventana):
        
        super().__init__(ventana)
        ventana.title("Concesionario de automóviles")
        #v.iconbitmap(r"C:\Users\jucer\OneDrive\Escritorio\Parser\carpetIMG.ico")
        #ventana.geometry("600x1024")
       
        self.treeview = ttk.Treeview(self)
        self.Carpeta = self.treeview.insert("", tk.END, text="Coches")
        
        

    

    def insertarNombreSubCarpeta(self,nombre):
        self.coche= self.treeview.insert(self.Carpeta, tk.END, text=nombre)
    
    def insertarMarcaDeAuto(self,marca):
        self.treeview.insert(self.coche, tk.END, text=marca)
    
    def insertarAño(self,año):
        self.treeview.insert(self.coche, tk.END, text=año)
    
    def insertarTipoDETrasmicion(self,transmision):
        self.treeview.insert(self.coche, tk.END, text=transmision)

    def insertarModoDeManejo(self,modoManejo):
        self.treeview.insert(self.coche, tk.END, text=modoManejo)


    
    #def mostrarArbol(self,nombre,marca,año,transmision):
     #  self.treeview.insert(Coche,self.contador, tk.END, text=nombre)
        
        
        
        
        
        
      #
        #Coche2=self.treeview.insert(Carpeta1, tk.END, text="Coche 2")
        #self.treeview.insert(Coche2, tk.END, text="Marca")
        #self.treeview.insert(Coche2, tk.END, text="Año")
        #Coche3=self.treeview.insert(Carpeta1, tk.END, text="Coche 3")
        #self.treeview.insert(Coche3, tk.END, text="Marca")
        #self.treeview.insert(Coche3, tk.END, text="Año")

    def mostrarArbol(self): 
        self.treeview.pack()
        self.pack()
