from auto import Auto

class AutoLogan(Auto):
    
    #def añadirModoDeManejo(self,modoDeManejo):
     #   self.__modoDeManejo__=modoDeManejo
    
    def __init__(self, nombre, marca, año, transmision, color,modoDeManejo):
        super().__init__(nombre, marca, año, transmision, color)
        self.__modoDeManejo__=modoDeManejo


    def getModoDeManejo(self):
        return self.__modoDeManejo__

    def toString(self):
        return super().toString(),self.__modoDeManejo__