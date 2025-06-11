# evaluador_de_formulas.py

def parsingExpresiones(expr: str):
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


def evaluar_expresion(expr: str):
    """
    Evalúa expresiones aritméticas con funciones como SUMA, RESTA, MAX, MIN, ABS.
    Soporta funciones anidadas.
    """
    expr = expr.strip()

    # Si es un número directo, lo convertimos y devolvemos
    if expr.replace('.', '', 1).lstrip('-').isdigit():
        return float(expr)

    # Si es una función, la procesamos
    nombre_funcion, argumentos = parsingExpresiones(expr)

    # Evaluamos recursivamente cada argumento
    argumentos_evaluados = [evaluar_expresion(arg) for arg in argumentos]

    # Ejecutamos según el nombre de la función
    if nombre_funcion == 'SUMA':
        return sum(argumentos_evaluados)
    elif nombre_funcion == 'RESTA':
        if len(argumentos_evaluados) < 2:
            raise ValueError("RESTA necesita al menos dos argumentos.")
        resultado = argumentos_evaluados[0]
        for arg in argumentos_evaluados[1:]:
            resultado -= arg
        return resultado
    elif nombre_funcion == 'MAX':
        return max(argumentos_evaluados)
    elif nombre_funcion == 'MIN':
        return min(argumentos_evaluados)
    elif nombre_funcion == 'ABS':
        if len(argumentos_evaluados) != 1:
            raise ValueError("ABS solo acepta un argumento.")
        return abs(argumentos_evaluados[0])
    else:
        raise ValueError(f"Función no reconocida: {nombre_funcion}")
