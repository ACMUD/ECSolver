from datetime import datetime

class ExcelCalculadora:
    # Método privado para validar que todos los argumentos sean números
    def __validar_numeros(self, *args):
        if not args:  # Si no se pasa ningún argumento
            raise ValueError("Se requiere al menos un número.")
        for arg in args:  # Se recorre cada argumento
            # Si alguno no es int ni float, lanza un error
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Argumento no numérico: {arg}")

    # Método para sumar todos los argumentos
    def suma(self, *args):
        self.__validar_numeros(*args)  # Validación de argumentos
        return sum(args)  # Retorna la suma

    # Método para sacar el promedio
    def promedio(self, *args):
        self.__validar_numeros(*args)
        return sum(args) / len(args)  # Suma y divide por la cantidad

    # Método que retorna el número más alto
    def maximo(self, *args):
        self.__validar_numeros(*args)
        return max(args)

    # Método que retorna el número más bajo
    def minimo(self, *args):
        self.__validar_numeros(*args)
        return min(args)

    # Método para multiplicar todos los argumentos
    def multiplicar(self, *args):
        self.__validar_numeros(*args)
        resultado = 1
        for num in args:  # Multiplica uno por uno
            resultado *= num
        return resultado

    # Método para dividir dos números
    def dividir(self, a, b):
        self.__validar_numeros(a, b)
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return a / b
# Se define la función para restar

def resta(*args):   #Se recibe n cantidad de valores
    argumentos = args      #Convierto "argumentos" en una tupla de los args

#Si no se entrega ningún valor
    if not args:
        return 0
# Verifico errores en los datos ingresados
    try:
# Realizo las operaciones para la resta
      resultado = argumentos[0]
      for h in argumentos[1:]:
          resultado -= h
      return resultado
    except (ValueError, TypeError):
      print("Al menos uno de los datos ingresados no es un número,\npor favor ingrese únicamente números")
# Se define la función para potencia

def potencia(*args):   #Se recibe 2 valores

#Si no se entrega ningún valor
    if not args:
        return 0

# Verifico errores en los datos ingresados
    try:
      #Si se reciben más de 2 argumentos
      if len(args) > 2:
        return print("Ingresa solo 2 argumentos")
      #Si se recibe solo 1 argumento
      if len(args) == 1:
        return print("Tienen que ser al menos 2 argumentos")
      #Si b es igual a 0
      if args[1] == 0:
        return 1
      #Si a es igual a 0
      if args[0] == 0:
        return 0
      #Si se eleva 0 a la 0
      if args[0] == 0 and args[1] == 0:
       return print("No se puede elevar 0 a la 0")

# Realizo las operaciones para la potencia
      resultado = args[0]**args[1]
      return resultado

    except (ValueError, TypeError):
      print("Ingresa únicamente números")
# Se define la función para raiz

def raiz(*args):   #Se recibe 1 valor o 2

#Si no se entrega ningún valor
    if not args:
        return 0

# Verifico errores en los datos ingresados
    try:

      #Si se reciben más de 2 argumentos
      if len(args) > 2:
        return print("Ingresa solo 2 argumentos")
      #Si la base es igual a 0
      if args[0] == 0:
        return 0
      #Si la base es negativa
      if args[0] < 0:
        return print("No se puede calcular la raiz negativa")

# Realizo las operaciones para la raiz

      #Si solo se recibe 1 dato (base, por defecto raiz cuadrada)
      if len(args) == 1:
        resultado = args[0]**(1/2)
        return resultado
      #Si se reciben 2 datos (base y raiz)
      if len(args) == 2:
        resultado = args[0]**(1/args[1])
        return resultado
      #Si se recibe la raíz como valor 0
      if len(args) == 2 and args[1] == 0:
        return print("No existe la raiz 0")

    except (ValueError, TypeError):
      print("Ingresa únicamente números")
#Se defina la función si

def si(*args):    #Se recibe solo 1 expresión (True/False) más dos opciones cualquiera

#Si no se entrega ningún valor
  if not args:
      return 0

# Verifico errores en los datos ingresados
  try:

    #Si se reciben más de 3 argumentos
    if len(args) > 3:
       return print("Ingresa solo 3 argumentos")
    #Si solo se reciben 2 argumentos
    if len(args) == 2:
       return print("Ingresa el menos 3 argumentos")

    #Elección si la condición es veradera o falsa
    if args[0]:
      return args[1]
    else:
      return args[2]

  except Exception as e:
    if type(e).__name__ == 'IndexError':
      print("Error: Ingresa al menos 3 argumentos")
    else:
      print(f"Error: {type(e).__name__} - {e}")
#Se defina la función y
def y(*args):    #Se recibe n argumentos

#Si no se entrega ningún valor
  if not args:
      return 0

# Verifico errores en los datos ingresados
  try:

    #Paso por cada argumento identificando si hay alguno falso

    Validación = None
    for arg in args:
      if arg:
        pass
      elif arg == False:
        Validación = False

    if Validación == None:
      Validación = True

    #Verifico si hubo alguno falso o no
    if Validación:
      return True
    else:
      return False

  except Exception as e:
    print(f"Error: {type(e).__name__} - {e}")
#Se defina la función o
def o(*args):    #Se recibe n argumentos

#Si no se entrega ningún valor
  if not args:
      return 0

# Verifico errores en los datos ingresados
  try:

    #Paso por cada argumento identificando si hay alguno verdadero

    Validación = None
    for arg in args:
      if arg:
        Validación = True
      elif arg == False:
        pass

    if Validación == None:
      Validación = False

    #Verifico si hubo alguno verdadero o no
    if Validación:
      return True
    else:
      return False

  except Exception as e:
    print(f"Error: {type(e).__name__} - {e}")
def validar_argumentos(args, tipos_aceptados=None, cantidad_minima=1):
    """
    Valida los argumentos recibidos para una función.
    """
    if len(args) < cantidad_minima:
        raise ValueError(f"Se requieren al menos {cantidad_minima} argumentos.")
    if tipos_aceptados:
        for i, arg in enumerate(args):
            if not isinstance(arg, tipos_aceptados) and arg is not None:
                raise TypeError(f"Argumento en posición {i} no es del tipo esperado.")

def CONTAR(*args):
    validar_argumentos(args, cantidad_minima=1)
    return sum(1 for arg in args if isinstance(arg, (int, float)))

def CONTARA(*args):
    validar_argumentos(args, cantidad_minima=1)
    return sum(1 for arg in args if arg is not None and arg != "")

def CONTAR_SI(rango, condicion):
    if not isinstance(rango, (list, tuple)):
        raise TypeError("El rango debe ser una lista o tupla.")
    if not callable(condicion):
        raise TypeError("La condición debe ser una función.")
    return sum(1 for elem in rango if condicion(elem))

def BUSCARV(valor, tabla, columna):
    if not isinstance(tabla, list) or not all(isinstance(fila, list) for fila in tabla):
        raise TypeError("La tabla debe ser una lista de listas.")
    for fila in tabla:
        if len(fila) <= columna:
            raise IndexError("Columna fuera de rango en alguna fila.")
        if fila[0] == valor:
            return fila[columna]
    raise ValueError("Valor no encontrado en la primera columna.")

def BUSCARH(valor, tabla, fila):
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

def CONCATENAR(*args):
    validar_argumentos(args, cantidad_minima=1)
    return ''.join(str(arg) for arg in args if arg is not None)
# ... Métodos de Mafe, Jeison y Gerson ...


# Validación de entradas - Funciones de DonGatoUD

def validar_cadenas(*args):
    """Valida que todos los argumentos sean cadenas de texto (strings).
    Lanza errores si no hay argumentos o si alguno no es string."""

    if not args:
        raise ValueError("Se requiere al menos una cadena.")
    for arg in args:
        if not isinstance(arg, str):
            raise TypeError(f"Argumento no es cadena: {arg}")

def validar_cadena_y_numero(cadena, numero):
    """Valida que el primer argumento sea string y el segundo sea entero positivo.
    Hecha para ser usada en izquierda() y derecha()."""

    if not isinstance(cadena, str):
        raise TypeError(f"El primer argumento debe ser una cadena: {cadena}")
    if not isinstance(numero, int):
        raise TypeError(f"El segundo argumento debe ser un número entero: {numero}")
    if numero < 0:
        raise ValueError("El número de caracteres no puede ser negativo.")


# Primer función DonGatoUD
def concat(*args):
    """Unión de las cadenas de texto recibidas.

    Validaciones para la entrada:
    - Debe recibir al menos una cadena
    - Todos los argumentos deben ser strings

    Ejemplo: concat("Hola", " ", "ACM") retorna "Hola ACM"
    """

    validar_cadenas(*args)
    return "".join(args) ## Se coloca "" para que no haya separaciones entre la concatenación


# Segunda función DonGatoUD
def izquierda(cadena, num_caracteres):
    """Extrae "n numero de caracteres" 'num_caracteres' desde la izquierda de una cadena.

    Validaciones para la entrada:
    - El primer argumento debe ser string
    - El segundo argumento debe ser entero positivo

    Ejemplo: izquierda("ACMUD", 2) retorna "ACM"
    """

    validar_cadena_y_numero(cadena, num_caracteres)
    if num_caracteres > len(cadena):
        return cadena  # Si pide más caracteres de los que hay, retorno toda la cadena # (manejo del error)
    return cadena[:num_caracteres]


# Tercera función DonGatoUD
def derecha(cadena, num_caracteres):
    """Extrae "n numero de caracteres" 'num_caracteres' desde la derecha de una cadena.

    Validaciones de la entrada:
    - El primer argumento debe ser string
    - El segundo argumento debe ser entero positivo

    Ejemplo: derecha("ACMUD", 2) retorna "UD"
    """

    validar_cadena_y_numero(cadena, num_caracteres)
    if num_caracteres > len(cadena):
        return cadena  # Si pide más caracteres de los que hay, retorno toda la cadena # (manejo del error)
    return cadena[-num_caracteres:]


# Cuarta función DonGatoUD
def largo(cadena):
    """Calcula la longitud de una cadena (número de caracteres).

    Validaciones de la entrada:
    - El argumento debe ser string

    Ejemplo: largo("ACMUD") retorna 5
    """

    if not isinstance(cadena, str):
        raise TypeError(f"El argumento debe ser una cadena: {cadena}")
    return len(cadena)


# Quinta función DonGatoUD
def ahora():
    """Retorna la fecha y hora actual en formato legible.

    No requiere argumentos ni validaciones especiales.

    Ejemplo: ahora() retorna "2025-06-01 23:59:12"
    """

    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Sexta función DonGatoUD
def hoy():
    """Retorna solo la fecha actual (sin hora).

    No requiere argumentos ni validaciones especiales.

    Ejemplo: hoy() retorna "2025-06-01"
    """

    return datetime.now().strftime("%d-%m-%Y")

################################ PRUEBAS DE USO ################################

def probar_calculadora():
    calc = ExcelCalculadora()

    print("--- CASOS DE PRUEBA ---\n")

    # SUMA
    try:
        print("Suma(1, 2, 3):", calc.suma(1, 2, 3))  # Esperado: 6
    except Exception as e:
        print("Error en suma:", e)

    # PROMEDIO
    try:
        print("Promedio(2, 4, 6):", calc.promedio(2, 4, 6))  # Esperado: 4.0
    except Exception as e:
        print("Error en promedio:", e)

    # MÁXIMO
    try:
        print("Máximo(10, 50, 20):", calc.maximo(10, 50, 20))  # Esperado: 50
    except Exception as e:
        print("Error en máximo:", e)

    # MÍNIMO
    try:
        print("Mínimo(5, 3, 9):", calc.minimo(5, 3, 9))  # Esperado: 3
    except Exception as e:
        print("Error en mínimo:", e)

    # MULTIPLICAR
    try:
        print("Multiplicar(2, 3, 4):", calc.multiplicar(2, 3, 4))  # Esperado: 24
    except Exception as e:
        print("Error en multiplicar:", e)

    # DIVIDIR normal
    try:
        print("Dividir(10, 2):", calc.dividir(10, 2))  # Esperado: 5.0
    except Exception as e:
        print("Error en dividir:", e)

    # DIVIDIR por cero
    try:
        print("Dividir(10, 0):", calc.dividir(10, 0))  # Esperado: Error
    except Exception as e:
        print("Error esperado en dividir por cero:", e)

    # SUMA con letras
    try:
        print("Suma('a', 2):", calc.suma('a', 2))  # Esperado: Error de tipo
    except Exception as e:
        print("Error esperado en suma con letra:", e)

if __name__ == "__main__":
    probar_calculadora()
# Ejemplos de uso
print("***Ejemplos de uso***\n")

#Función de resta
resultado = resta(20, 5, 2, 3, 4)
print(f"Función resta - (20, 5, 2, 3, 4):",resultado)

#Función de potencia
resultado = potencia(10, 3)
print(f"Función potencia - (10, 3):",resultado)

#Función de raiz
resultado = raiz(8, 3)
print(f"Función raiz - (8, 3):",resultado)

#Función si
resultado = si(1==0, "Eso está bien", "Eso está mal")
print(f"Función si - (1==0, 'Verdadero', 'Falso'):",resultado)

#Función y
resultado = y(True, True, False, True)
print(f"Función y - (True, True, False, True):",resultado)

#Función o
resultado = o(True, False, False, False)
print(f"Función o - (True, False, False, False):",resultado)

#Función contar
def test_contar():
    assert CONTAR(1, 2.5, "texto", None) == 2

#Función contará
def test_contara():
    assert CONTARA(1, "", None, "hola", 0) == 4

#Función contar si
def test_contar_si():
    assert CONTAR_SI([1, 2, 3, 4], lambda x: x > 2) == 2

#Función buscarv
def test_buscarv():
    tabla = [["Ana", 30], ["Luis", 25]]
    assert BUSCARV("Luis", tabla, 1) == 25

#Función buscarh
def test_buscarh():
    tabla = [["Nombre", "Edad"], ["Ana", 30]]
    assert BUSCARH("Edad", tabla, 1) == 30

#Función concatenar
def test_concatenar():
    assert CONCATENAR("Hola", " ", "mundo", "!") == "Hola mundo!"

# Ejemplos de uso con print()

# Función concat
print(concat("Hola", " ", "mundo"))  # Output: Hola mundo
print(concat("ACM", "UD", " 2025"))  # Output: ACMUD 2025

# Función izquierda
print(izquierda("ACMUD", 3))  # Output: ACM
print(izquierda("Python", 2))  # Output: Py

# Función derecha
print(derecha("ACMUD", 2))  # Output: UD
print(derecha("Programación", 4))  # Output: ción

# Función largo
print(largo("ACMUD"))  # Output: 5
print(largo("Hola mundo"))  # Output: 10

# Función ahora
print(ahora())  # Output: 04-06-2025 21:59:12 (fecha y hora actual)

# Función hoy
print(hoy())  # Output: 04-06-2025 (solo fecha actual)