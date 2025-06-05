# Function Extension Module
Este módulo permite **registrar, evaluar, guardar y cargar** de forma segura funciones personalizadas provistas por el usuario.

## Caracteristicas
- Registro de funciones Python puras.
- Validación contra palabras clave peligrosas (`os`, `eval`, `exec`, etc.).
- Prevención de nombres reservados (`SUM`, `IF`, `AVG`, etc.).
- Evaluación de funciones con argumentos dinámicos.
- Serialización y deserialización de funciones en formato JSON.

## Estructura
- `FunctionRegistry`: Clase principal para registrar y evaluar funciones.
- `FunctionSave`: Clase auxiliar para guardar y cargar funciones desde archivos JSON.

# Uso 

## Crear Registro
registry = FunctionRegistry()

## Registrar una función
def suma(a, b):
    return a + b

registry.register("suma", suma)

## Evaluar la función
resultado = registry.evaluate("suma", 2, 3)
print(resultado)  # 5

## Guardar en JSON
FunctionSave.save_functions(registry, "mis_funciones.json")

## Cargar del JSON
**No implementado**