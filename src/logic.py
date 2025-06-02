import re
#El interprete de las expresiones brindadas 
class logic:

    def _init_(self,texto):
        self.texto=texto
        self.division=""
        self.constantes=[]
        self.funciones=[]
        self.referencias=[]
        self.value= False;
    
    def funcionesFun(self):
        #Clasificacion de las funciones presentes, solo despues del igual
        try:
            #parte de interes, despues de = 
            formula=self.division[1]
            
            #buscar las funciones con re 
            #pattern de las funciones es con mayuscula
            pattern = r"\b([A-Z]+)\s*\("
            #busca todas las funciones por el pattern que contiene 

            self.funciones= re.findall(pattern,formula)
        except IndexError:
            print("no se ecnontro ninguna funcion asignada")
          
        except Exception as e:
            print(f"Ocurrio un error en el proceso de clasificacion {e}")
    
    def constantesFun(self):
        #clasificacion de constantes
        try: 
            #las cosntantes solo se encuentran despues del igual 
            formula= self.division[1]
            #patern de las constantes
            pattern = r'[-+]?\b\d+(?:\.\d+)?\b'
            self.constantes = re.findall(pattern, formula)
        except IndexError:
            print("No se encontro ninguna constante")
        except Exception as e: 
            print(f"Ocurrio un error de ejecucion {e}")

    def referenciasFun(self):
        #Clasificacion de referencias
        try:
            #Clasificacion mediante el pattern
            formula= self.division[1]
            pattern = r'\b[A-Z]{1,3}[1-9][0-9]{0,4}\b'
            self.referencias = re.findall(pattern, formula)
        except IndexError:
            print("No se encontro ninguna constante")
        except Exception as e: 
            print(f"Ocurrio un error de ejecucion {e}")


        
    def imprimirCadenaFun(self):
        if self.value==True:
            #Mostrar las dos partes del igual al usuario
            print(f"la cadena esta dividiad en {self.division}, funciones {self.funciones}, constantes {self.constantes},referencias{self.referencias}")
        else:
            #cuando no se cumpe la expresion repetir el proceso
            print("No pudes imprimr nada el valor ingreado no corresponde a una exprecion logica ")


    def clasificacionFun(self):
        #Verifcar si hay una expresion de igualdad
        for i in self.texto:
            if i=="=":
                self.value=True
        #recorrre la cadena en busca de una expresion valida 
        #clasificacion de la primera igualdad
        try:
            if self.value==True:
                self.division=self.texto.split(sep="=",maxsplit=2)
        except:
            print("No se encuentra ninguna expresion de igualdad, intentelo de nuevo")
            return
        self.funcionesFun()
        self.constantesFun()
        self.referenciasFun()
        self.imprimirCadenaFun()

        
        
        

#parte para hacer el test de la prueba logica
while True:
    test = input("Ingrea tu expresion a valorar: ")
    prueba = logic(test)
    prueba.clasificacionFun()
    if(prueba.value==True):
        break