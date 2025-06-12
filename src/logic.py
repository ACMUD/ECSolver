import re

# El interprete de las expresiones brindadas 
class Logic:
    def __init__(self, texto):
        self.texto = texto.strip()
        self.division = ""
        self.constantes = []
        self.funciones = []
        self.referencias = []
        self.rangos = []
        self.value = False

    def funcionesFun(self):
        try:
            formula = self.division[1].upper()  # Normalizar a mayúsculas
            pattern = r"\b([A-Z]+)\s*\("
            self.funciones = re.findall(pattern, formula)
        except IndexError:
            print("No se encontró ninguna función")
        except Exception as e:
            print(f"Error en funciones: {e}")

    def constantesFun(self):
        try:
            formula = self.division[1]
            pattern = r'[-+]?\b\d+(?:\.\d+)?\b'
            self.constantes = re.findall(pattern, formula)
        except IndexError:
            print("No se encontró ninguna constante")
        except Exception as e:
            print(f"Error en constantes: {e}")

    def referenciasFun(self):
        try:
            formula = self.division[1].upper()
            # Detectar rangos como A1:B34
            self.rangos = re.findall(r'\b[A-Z]{1,3}[1-9][0-9]{0,4}:[A-Z]{1,3}[1-9][0-9]{0,4}\b', formula)
            # Detectar referencias simples (excluyendo las que ya están en rangos)
            todas = re.findall(r'\b[A-Z]{1,3}[1-9][0-9]{0,4}\b', formula)
            partes_de_rangos = [celda for r in self.rangos for celda in r.split(":")]
            self.referencias = [ref for ref in todas if ref not in partes_de_rangos]
        except Exception as e:
            print(f"Error en referencias: {e}")

    def imprimirCadenaFun(self):
        if self.value:
            print("\n--- Resultado ---")
            print(f"Funciones encontradas: {self.funciones}")
            print(f"Constantes encontradas: {self.constantes}")
            print(f"Referencias individuales: {self.referencias}")
            print(f"Rangos detectados: {self.rangos}")
            print("------------------\n")
        else:
            print("No puedes imprimir nada. La fórmula no empieza con '='.")

    def direccionamientoFun(self):
        funciones_basicas = {"SUMA", "MAX", "MIN", "PROMEDIO"}
        funciones_ext = {"SI", "CONTAR.SI", "CONCATENAR"}

        print("\n--- Clasificación y Direccionamiento ---")
        for constante in self.constantes:
            print(f"🔹 Constante '{constante}' → Evaluación directa")

        for referencia in self.referencias:
            print(f"🔹 Referencia '{referencia}' → Resolución de referencia")

        for rango in self.rangos:
            print(f"🔹 Rango '{rango}' → Resolución de referencia (rango)")

        for funcion in self.funciones:
            if funcion in funciones_basicas:
                print(f"🔹 Función básica '{funcion}' → Evaluación funcional")
            elif funcion in funciones_ext:
                print(f"🔹 Función extendida '{funcion}' → Evaluación funcional")
            else:
                print(f"❌ Función '{funcion}' no reconocida → Error: función desconocida")

        print("-----------------------------------------\n")
    

    def clasificacionFun(self):
        if "=" in self.texto:
            self.value = True
        else:
            print("❌ La fórmula no contiene '='.")
            return

        try:
            self.division = self.texto.split("=", maxsplit=1)
            self.funcionesFun()
            self.constantesFun()
            self.referenciasFun()
            self.imprimirCadenaFun()
            self.direccionamientoFun()
        except Exception as e:
            print(f"Ocurrió un error general: {e}")


        

        
#parte para hacer el test de la prueba logica
while True:
    test = input("Ingrese su expresión a valorar (ej: =SUMA(1,A1,B2:B5)): ")
    prueba = Logic(test)
    prueba.clasificacionFun()
    if prueba.value:
        break
