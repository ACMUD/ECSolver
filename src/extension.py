# extension.py

# Este módulo permite al usuario registrar funciones personalizadas
# y luego usarlas desde otras partes del programa.
import types
import inspect

class FunctionRegistry:
    """
    Clase para registrar y evaluar funciones personalizadas de forma segura.

    Asegura que las funciones registradas:
    - No usen nombres reservados como 'SUM', 'IF', etc.
    """
    def __init__(self):
        """Inicializa el registro con funciones permitidas"""
        self._functions = {}
        self._reserved = {"SUM", "AVG", "IF", "MAX", "MIN"} 
        
    def register(self, name: str, func):
        """
        Registra una función en el sistema si es segura, no usa el nombre de una función reservada.

        Parámetros:
            name (str): Nombre de la función.
            func (function): Objeto de función a registrar.

        Retorna:
            None
        """
        if name.upper() in self._reserved:
            print(f"Error: El nombre '{name}' está reservado y no se puede usar.")
            return
        if not isinstance(func, types.FunctionType):
            print(f"Error: lo que intentas registrar no es una función.")
            return

        print(f"Registrando función {name}")
        source = inspect.getsource(func)
        self._functions[name] = {"func": func, "source": source}
        print(f"Función '{name}' registrada con éxito.")

    def evaluate(self, name, *args):
        """
        Evalúa una función registrada con los argumentos dados.

        Parámetros:
            name (str): Nombre de la función.
            *args: Argumentos para la función.

        Retorna:
            Resultado de la función, o None si hay error o no está registrada.
        """
        if name not in self._functions:
            print(f"Error: La función '{name}' no ha sido registrada.")
            return
        try:
            result = self._functions[name]["func"](*args)
            return result
        except Exception as e:
            print(f"Error: fallo al ejecutar la función '{name}':", e)
            return

    def get_registered_functions(self):
        """
        Retorna una lista de funciones registradas, incluyendo nombre y código fuente.

        Retorna:
            list[dict]: Lista de funciones con claves 'name' y 'source'.
        """
        return [
            {"name": name, "source": data["source"]}
            for name, data in self._functions.items()
        ]
    