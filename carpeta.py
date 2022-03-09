
from asyncio.windows_events import NULL

import tkinter as tk
from tkinter import BOTH, ttk

class ArbolDeAutos(ttk.Frame):
    
    def __init__(self, ventana):
        
        super().__init__(ventana)
        ventana.title("Explorador de automóviles")
        #v.iconbitmap(r"C:\Users\jucer\OneDrive\Escritorio\Parser\carpetIMG.ico")
        ventana.geometry("400x400")
        ventana.iconbitmap(r"C:\Users\WALTER\Downloads\explorador (2).ico")
        self.icono=tk.PhotoImage(file="folder.png")
        self.icono2=tk.PhotoImage(file="file.png")
        self.treeview = ttk.Treeview(self)
        self.Carpeta = self.treeview.insert("", tk.END, text="Coches",image=self.icono)
        

    def insertarNombreSubCarpeta(self,nombre):
        self.coche= self.treeview.insert(self.Carpeta, tk.END, text=nombre,image=self.icono)
    
    def insertarMarcaDeAuto(self,marca):
        self.treeview.insert(self.coche, tk.END, text=marca,image=self.icono2)
    
    def insertarAño(self,año):
        self.treeview.insert(self.coche, tk.END, text=año,image=self.icono2)
    
    def insertarTipoDETrasmicion(self,transmision):
        self.treeview.insert(self.coche, tk.END, text=transmision,image=self.icono2)

    def insertarModoDeManejo(self,modoManejo):
        self.treeview.insert(self.coche, tk.END, text=modoManejo,image=self.icono2)


    
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
        self.treeview.pack(fill = BOTH, expand = True)
        self.pack(fill = BOTH, expand = True)
