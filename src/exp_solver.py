# exp_solver.py
from typing import List, Tuple, Any, Union

class ExpSolver:
    """
    Módulo ExpSolver - Evaluador de expresiones con funciones.
    
    Actúa como puente entre el Solver y los módulos Basic/Extension.
    Recibe expresiones sin referencias a celdas y las evalúa.
    """
    
    def __init__(self, moduloBasic=None, moduloExtension=None):
        self.basic = moduloBasic
        self.extension = moduloExtension
    
    def parsingExpresiones(self, expr: str) -> Tuple[str, List[str]]:
        """
        Hace el parsing de expresiones como 'SUMA(10, 5)' o 'MAX(3, MIN(2, 5))'
        Devuelve el nombre de la función y una lista de argumentos como strings.
        """
        expr = expr.strip()

        if '(' not in expr or not expr.endswith(')'):
            raise ValueError(f'La expresión: {expr} es inválida')

        primerParentesis = expr.index('(')
        nombreFuncion = expr[:primerParentesis].strip().upper()
        stringArgumento = expr[primerParentesis + 1: -1].strip()

        argumentos = []
        conteoParentesis = 0
        argumentoActual = ''

        for c in stringArgumento:
            if c == ',' and conteoParentesis == 0:
                argumentos.append(argumentoActual.strip())
                argumentoActual = ''
            else:
                if c == '(':
                    conteoParentesis += 1
                elif c == ')':
                    conteoParentesis -= 1
                argumentoActual += c

        if argumentoActual:
            argumentos.append(argumentoActual.strip())

        return nombreFuncion, argumentos
    
    def validarArgumentos(self, nombreFuncion: str, argumentos: List[Any]) -> None:
        """
        Valida que los argumentos sean del tipo y cantidad correctos.
        """
        # Validación de tipos - todos deben ser numéricos
        for i, arg in enumerate(argumentos):
            if not isinstance(arg, (int, float)):
                raise ValueError(
                    f"Error de tipo en {nombreFuncion}: argumento en posición {i+1} "
                    f"debe ser numérico, se recibió '{arg}'"
                )
    
    def obtenerFuncion(self, nombreFuncion: str):
        """
        Obtiene la función del módulo correspondiente (Basic o Extension).
        """
        # Buscar en Basic
        if self.basic and hasattr(self.basic, 'tieneFuncion'):
            if self.basic.tieneFuncion(nombreFuncion):
                return self.basic.obtenerFuncion(nombreFuncion)
        
        # Buscar en Extension
        if self.extension and hasattr(self.extension, 'tieneFuncion'):
            if self.extension.tieneFuncion(nombreFuncion):
                return self.extension.obtenerFuncion(nombreFuncion)
        
        # Si no se encuentra, usar implementación temporal
        funcionesTemporales = {
            'SUMA': lambda *args: sum(args),
            'RESTA': lambda a, *b: a - sum(b) if b else a,
            'MAX': max,
            'MIN': min,
            'ABS': abs,
            'PROMEDIO': lambda *args: sum(args) / len(args) if args else 0,
            'MULTIPLICAR': lambda *args: eval('*'.join(map(str, args))),
            'DIVIDIR': lambda a, b: a / b if b != 0 else (_ for _ in ()).throw(ValueError("División por cero")),
            'POTENCIA': lambda base, exp: base ** exp,
            'RAIZ': lambda n: n ** 0.5 if n >= 0 else (_ for _ in ()).throw(ValueError("Raíz de número negativo"))
        }
        
        if nombreFuncion in funcionesTemporales:
            return funcionesTemporales[nombreFuncion]
        
        raise ValueError(f"Función desconocida: {nombreFuncion}")
    
    def evaluarExpresion(self, expr: str) -> Union[float, int]:
        """
        Evalúa expresiones aritméticas con funciones como SUMA, RESTA, MAX, MIN, ABS.
        Soporta funciones anidadas.
        """
        expr = expr.strip()

        # Si es un número directo, lo convertimos y devolvemos
        try:
            return float(expr)
        except ValueError:
            pass

        # Si es una función, la procesamos
        nombreFuncion, argumentos = self.parsingExpresiones(expr)

        # Evaluamos recursivamente cada argumento
        argumentosEvaluados = []
        for arg in argumentos:
            valorEvaluado = self.evaluarExpresion(arg)
            argumentosEvaluados.append(valorEvaluado)
        
        # Validamos los argumentos
        self.validarArgumentos(nombreFuncion, argumentosEvaluados)
        
        # Obtenemos y ejecutamos la función
        funcion = self.obtenerFuncion(nombreFuncion)
        
        try:
            resultado = funcion(*argumentosEvaluados)
            return resultado
        except Exception as e:
            raise ValueError(f"Error ejecutando {nombreFuncion}: {str(e)}")
        


def parsingExpresiones(expr: str):
    solver = ExpSolver()
    return solver.parsingExpresiones(expr)

def evaluar_expresion(expr: str):
    solver = ExpSolver()
    return solver.evaluarExpresion(expr)