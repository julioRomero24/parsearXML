
import tkinter as tk
from tkinter import ttk

class Concesionario(ttk.Frame):
    def __init__(self, v):
        super().__init__(v)
        v.title("Concesionario de automóviles")
        #v.iconbitmap(r"C:\Users\jucer\OneDrive\Escritorio\Parser\carpetIMG.ico")
        v.geometry("600x600")
        self.treeview = ttk.Treeview(self)
        Carpeta1 = self.treeview.insert("", tk.END, text="Coches")
        Coche1= self.treeview.insert(Carpeta1, tk.END, text="Coche 1")
        self.treeview.insert(Coche1, tk.END, text="Marca")
        self.treeview.insert(Coche1, tk.END, text="Año")
        Coche2=self.treeview.insert(Carpeta1, tk.END, text="Coche 2")
        self.treeview.insert(Coche2, tk.END, text="Marca")
        self.treeview.insert(Coche2, tk.END, text="Año")
        Coche3=self.treeview.insert(Carpeta1, tk.END, text="Coche 3")
        self.treeview.insert(Coche3, tk.END, text="Marca")
        self.treeview.insert(Coche3, tk.END, text="Año")
        
        self.treeview.pack()
        self.pack()
v = tk.Tk()
app = Concesionario(v)
app.mainloop()
v.mainloop()