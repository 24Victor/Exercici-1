class Dad:
    #Constructor de la classe Dad introduim el nom complet predeterminat del pare
    def __init__(self, firstName="Victor", lastName="Zheng", lastName2="Giraldo"):
        #Com en aquest cas es opcional, ficarem per default un name de que en cas que no proporcionen un valor utilitzar el default del consturctor
        # y com no volem que es modifique ficarem __ per a que sigui privat
        self.__firstName = firstName
        self.__lastName = lastName
        self.__lastName2 = lastName2
        #En el atribut name, ens mostrara el nom complet
        self.__name = f"{self.__firstName} {self.__lastName} {self.__lastName2}"
    
    def getDadFirstName(self):
        return self.__firstName
    
    def getDadLastName(self):
        return self.__lastName
    
    def getDadFullName(self):
        return self.__name
    
class Mom:
    def __init__(self, firstName="Sara", lastName="Moreno", lastName2="Izquierdo"):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__lastName2 = lastName2
        self.__name = f"{self.__firstName} {self.__lastName} {self.__lastName2}"
        
    def getMomFirstName(self):
        return self.__firstName
    
    def getMomLastName(self):
        return self.__lastName
    
    def getMomFullName(self):
        return self.__name
        
class Child(Dad, Mom):
    def __init__(self, name):
        self.__name = name
        #Cridem la classe Dad en el qual al no passarli uns valors utilitzara els valors per defecte establits en Dad, i com
        Dad.__init__(self)
        Mom.__init__(self)
        
    def getFullName(self):
        #de la classe child, com no trobara el metode getDadLastName, el buscare en classe Dad i la trobara, i amb Mom igual
        return f"El meu nom complet és {self.__name} {self.getDadLastName()} {self.getMomLastName()}"
    
    def getNameFullDad(self):
        return f"El nom del meu pare és {self.getDadFullName()}"
    
    def getNameFullMom(self):
        return f"El nom complet de la meva mare és {self.getMomFullName()}"
    
# Test del código
child = Child("Marius")
print(child.getFullName())
print(child.getDadFullName())
print(child.getMomFullName())