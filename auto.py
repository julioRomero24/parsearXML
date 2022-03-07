

class Auto():

    
        


    def __init__(self,nombre,marca,año,transmision,color):
        self.__nombre__=nombre
        self.__marca__=marca 
        self.__año__=año
        self.__transmision__=transmision
        self.__color__=color

    

    def getNombre(self):
        return  self.__nombre__

    def getMarca(self):
        return self.__marca__

    def getAño(self):
        return self.__año__

    def getTransmision(self):
        return self.__transmision__
    
    def getColor(self):
        return self.__color__
       

    def toString(self):
        return (self.__nombre__,self.__marca__,self.__año__,self.__transmision__,self.__color__)
        #print(self.__nombre__,self.__marca__,self.__año__,self.__transmision__,self.__color__)


    