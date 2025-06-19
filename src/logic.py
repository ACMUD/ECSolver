import re

class Logic:
    """
    Clase Logic para interpretar y clasificar elementos léxicos en una fórmula de Excel.

    Atributos:
        texto (str): La fórmula o expresión a analizar.
        division (list): Texto dividido por el símbolo '='.
        constantes (list): Lista de constantes numéricas.
        funciones (list): Lista de funciones detectadas.
        referencias (list): Lista de referencias individuales.
        rangos (list): Lista de rangos de celdas.
        value (bool): Indica si la fórmula es válida (empieza con '=').
    """

    def __init__(self, texto):
        """Inicializa una instancia con la fórmula dada."""
        self.texto = texto.strip()
        self.division = ""
        self.constantes = []
        self.funciones = []
        self.referencias = []
        self.rangos = []
        self.value = False

    def funcionesFun(self):
        """Detecta y registra funciones en la fórmula."""
        formula = self.division[1].upper()
        pattern = r"\b([A-Z]+)\s*\("
        self.funciones = re.findall(pattern, formula)

    def constantesFun(self):
        """Detecta y registra constantes numéricas en la fórmula."""
        formula = self.division[1]
        pattern = r'[-+]?\b\d+(?:\.\d+)?\b'
        self.constantes = re.findall(pattern, formula)

    def referenciasFun(self):
        """Detecta y registra referencias y rangos en la fórmula."""
        formula = self.division[1].upper()
        self.rangos = re.findall(r'\b[A-Z]{1,3}[1-9][0-9]{0,4}:[A-Z]{1,3}[1-9][0-9]{0,4}\b', formula)
        todas = re.findall(r'\b[A-Z]{1,3}[1-9][0-9]{0,4}\b', formula)
        partes_de_rangos = [celda for r in self.rangos for celda in r.split(":")]
        self.referencias = [ref for ref in todas if ref not in partes_de_rangos]

    def manejarErrores(self):
        """Valida las funciones detectadas, lanzando error si son desconocidas."""
        funciones_validas = {"SUMA", "MAX", "MIN", "PROMEDIO", "SI", "CONTAR.SI", "CONCATENAR"}
        for funcion in self.funciones:
            if funcion not in funciones_validas:
                raise ValueError(f"Función desconocida: {funcion}")

    def direccionamientoFun(self):
        """
        Clasifica cada elemento léxico detectado según el orden de evaluación requerido.

        Retorna:
            dict: Clasificación ordenada de los elementos léxicos.
        """
        funciones_basicas = {"SUMA", "MAX", "MIN", "PROMEDIO"}
        funciones_ext = {"SI", "CONTAR.SI", "CONCATENAR"}

        clasificacion = {
            "constantes": [(c, "Evaluación directa") for c in self.constantes],
            "referencias": [(r, "Resolución de referencia") for r in self.referencias],
            "rangos": [(rg, "Resolución de referencia (rango)") for rg in self.rangos],
            "funciones": [
                (f, "Evaluación funcional básica") if f in funciones_basicas else
                (f, "Evaluación funcional extendida") if f in funciones_ext else
                (f, "Desconocida") for f in self.funciones
            ]
        }

        orden_evaluacion = ["constantes", "referencias", "rangos", "funciones"]
        return {key: clasificacion[key] for key in orden_evaluacion}

    def clasificacionFun(self):
        """
        Valida, analiza y clasifica la fórmula completa.

        Retorna:
            dict: Resultado estructurado con clasificación y descripción de elementos.

        Lanza:
            ValueError: Si la fórmula no es válida (no comienza con '=').
        """
        if "=" not in self.texto:
            raise ValueError("La fórmula no comienza con '='")
        self.value = True
        self.division = self.texto.split("=", maxsplit=1)
        self.funcionesFun()
        self.constantesFun()
        self.referenciasFun()
        self.manejarErrores()
        return self.direccionamientoFun()


# Ejemplo de ejecución
test = "=SUMA(1, A1, B2:B5)"
logica = Logic(test)
try:
    resultado = logica.clasificacionFun()
    print("--- Resultado ---")
    for tipo, elementos in resultado.items():
        for elemento, descripcion in elementos:
            print(f"🔹 {tipo.capitalize()} '{elemento}' → {descripcion}")
except ValueError as ve:
    print(f"Error: {ve}")
