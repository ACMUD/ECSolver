from datetime import datetime

class ExcelCalculadora:
    
    # Validación de que todos los argumentos sean números (int o float)
    def __validar_numeros(self, *args):
        if not args:
            raise ValueError("Se requiere al menos un número.")
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Argumento no numérico: {arg}")

    # Validación de que todos los argumentos sean cadenas de texto
    def __validar_cadenas(self, *args):
        if not args:
            raise ValueError("Se requiere al menos una cadena.")
        for arg in args:
            if not isinstance(arg, str):
                raise TypeError(f"Argumento no es cadena: {arg}")

    # Validación combinada: cadena y número entero positivo
    def __validar_cadena_y_numero(self, cadena, numero):
        if not isinstance(cadena, str):
            raise TypeError(f"El primer argumento debe ser una cadena: {cadena}")
        if not isinstance(numero, int):
            raise TypeError(f"El segundo argumento debe ser un número entero: {numero}")
        if numero < 0:
            raise ValueError("El número de caracteres no puede ser negativo.")

    # Validación general con control de tipos y cantidad mínima
    def __validar_argumentos(self, args, tipos_aceptados=None, cantidad_minima=1):
        if len(args) < cantidad_minima:
            raise ValueError(f"Se requieren al menos {cantidad_minima} argumentos.")
        if tipos_aceptados:
            for i, arg in enumerate(args):
                if not isinstance(arg, tipos_aceptados) and arg is not None:
                    raise TypeError(f"Argumento en posición {i} no es del tipo esperado.")

    # --------- Métodos matemáticos ---------

    # Suma de números
    def suma(self, *args):
        self.__validar_numeros(*args)
        return sum(args)

    # Promedio de números
    def promedio(self, *args):
        self.__validar_numeros(*args)
        return sum(args) / len(args)

    # Valor máximo
    def maximo(self, *args):
        self.__validar_numeros(*args)
        return max(args)

    # Valor mínimo
    def minimo(self, *args):
        self.__validar_numeros(*args)
        return min(args)

    # Multiplicación de números
    def multiplicar(self, *args):
        self.__validar_numeros(*args)
        resultado = 1
        for num in args:
            resultado *= num
        return resultado

    # División con validación de división por cero
    def dividir(self, a, b):
        self.__validar_numeros(a, b)
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return a / b

    # Resta de números
    def resta(self, *args):
        self.__validar_numeros(*args)
        if not args:
            return 0
        resultado = args[0]
        for h in args[1:]:
            resultado -= h
        return resultado

    # Potenciación
    def potencia(self, base, exponente):
        self.__validar_numeros(base, exponente)
        if exponente == 0:
            return 1
        if base == 0:
            return 0
        return base ** exponente

    # Cálculo de raíz n-ésima
    def raiz(self, base, indice=2):
        self.__validar_numeros(base, indice)
        if base < 0:
            raise ValueError("No se puede calcular la raíz de un número negativo.")
        if indice == 0:
            raise ValueError("No existe la raíz 0.")
        return base ** (1 / indice)

    # --------- Métodos lógicos ---------

    # Simula la función SI(condición, valor_verdadero, valor_falso)
    def si(self, condicion, valor_verdadero, valor_falso):
        return valor_verdadero if condicion else valor_falso

    # Evaluación lógica tipo Y
    def y(self, *args):
        return all(args)

    # Evaluación lógica tipo O
    def o(self, *args):
        return any(args)

    # --------- Métodos de conteo y búsqueda ---------

    # Cuenta los elementos que son números
    def CONTAR(self, *args):
        self.__validar_argumentos(args, cantidad_minima=1)
        return sum(1 for arg in args if isinstance(arg, (int, float)))

    # Cuenta elementos no vacíos ni None
    def CONTARA(self, *args):
        self.__validar_argumentos(args, cantidad_minima=1)
        return sum(1 for arg in args if arg is not None and arg != "")

    # Cuenta elementos que cumplen una condición en un rango
    def CONTAR_SI(self, rango, condicion):
        if not isinstance(rango, (list, tuple)):
            raise TypeError("El rango debe ser una lista o tupla.")
        if not callable(condicion):
            raise TypeError("La condición debe ser una función.")
        return sum(1 for elem in rango if condicion(elem))

    # Búsqueda vertical (tipo BUSCARV)
    def BUSCARV(self, valor, tabla, columna):
        if not isinstance(tabla, list) or not all(isinstance(fila, list) for fila in tabla):
            raise TypeError("La tabla debe ser una lista de listas.")
        for fila in tabla:
            if len(fila) <= columna:
                raise IndexError("Columna fuera de rango en alguna fila.")
            if fila[0] == valor:
                return fila[columna]
        raise ValueError("Valor no encontrado en la primera columna.")

    # Búsqueda horizontal (tipo BUSCARH)
    def BUSCARH(self, valor, tabla, fila):
        if not isinstance(tabla, list) or not all(isinstance(f, list) for f in tabla):
            raise TypeError("La tabla debe ser una lista de listas.")
        if len(tabla) == 0 or len(tabla[0]) == 0:
            raise ValueError("La tabla no puede estar vacía.")
        if fila >= len(tabla):
            raise IndexError("Número de fila fuera de rango.")
        for i, encabezado in enumerate(tabla[0]):
            if encabezado == valor:
                return tabla[fila][i]
        raise ValueError("Valor no encontrado en la primera fila.")

    # Concatenación de elementos como texto
    def CONCATENAR(self, *args):
        self.__validar_argumentos(args, cantidad_minima=1)
        return ''.join(str(arg) for arg in args if arg is not None)

    # --------- Métodos de texto ---------

    # Concatenación de cadenas (solo acepta strings)
    def concat(self, *args):
        self.__validar_cadenas(*args)
        return "".join(args)

    # Extrae caracteres desde el inicio (izquierda)
    def izquierda(self, cadena, num_caracteres):
        self.__validar_cadena_y_numero(cadena, num_caracteres)
        if num_caracteres > len(cadena):
            return cadena
        return cadena[:num_caracteres]

    # Extrae caracteres desde el final (derecha)
    def derecha(self, cadena, num_caracteres):
        self.__validar_cadena_y_numero(cadena, num_caracteres)
        if num_caracteres > len(cadena):
            return cadena
        return cadena[-num_caracteres:]

    # Devuelve la longitud de una cadena
    def largo(self, cadena):
        if not isinstance(cadena, str):
            raise TypeError(f"El argumento debe ser una cadena: {cadena}")
        return len(cadena)

    # --------- Métodos de fecha y hora ---------

    # Devuelve fecha y hora actual con formato
    def ahora(self):
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Devuelve solo la fecha actual
    def hoy(self):
        return datetime.now().strftime("%d-%m-%Y")