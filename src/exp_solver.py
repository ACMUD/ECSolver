

def parsingExpresiones(expr: str):
    """
    Hace el parsing de las expresiones como 'SUMA(10, 5)' para separar y devolver
    el nombre de la funcion y una lista de sus argumentos en forma de strings
    """
    #Funcion para eliminar espacios en blanco al inicio y final de la cadena
    expr = expr.strip() 

    #Se valida que la cadena contenga al menos un '(' y que termine con un ')'
    if '(' not in expr or not expr.endswith(')'):
        raise ValueError(f'La expresión: {expr} es inválida')
    
    #Busca la posicion del primer parentesis
    primerParentesis = expr.index('(')

    #Se obtiene la subcadena que contiene el nombre de la funcion, es lo que hay antes del '('
    nombreFuncion = expr[:primerParentesis].strip().upper()
    
    #Se obtiene la subcadena que contiene los argumentos, lo que hay entre '(' y ')'
    stringArgumento = expr[primerParentesis + 1: -1].strip()

    argumentos = [] 
    conteoParentesis = 0 #Contamos la cantidad de parentesis para funciones anidadas
    argumentoActual = ''

    """
    Bucle para recorrer la cadena de argumentos caracter por caracter:
    • Conteo 0 significa que no estamos dentro de parentesis anidados
    • Si hay una ',' y el conteo es 0, significa que terminamos un argumento, se agrega a args
    • Si no es ',' o estamos dentro de parentesis anidados, se agrega a argumento actual
    • Se actualiza el conteo para parentesis abiertos o cerrados
    """

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
    #Puede haber algun elemento acumulado al terminar, si lo hay, lo agregamos
    if argumentoActual:
        argumentos.append(argumentoActual.strip())

    return nombreFuncion, argumentos

