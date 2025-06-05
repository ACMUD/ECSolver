# 🧮 Archivo: `logic.py`

Este archivo implementa una clase llamada `Logic` en Python, la cual sirve como un **intérprete básico de expresiones tipo Excel**. Su propósito es descomponer una fórmula dada en sus partes fundamentales: funciones, constantes, referencias a celdas y rangos.

---

## ✨ Funcionalidad del archivo

Al ejecutar el script, el usuario puede ingresar una fórmula por consola (por ejemplo: `=SUMA(1,A1,B2:B5)`), y el programa identificará automáticamente:

- Funciones utilizadas (`SUMA`)
- Números constantes (`1`)
- Referencias a celdas individuales (`A1`)
- Rangos de celdas (`B2:B5`)

---

## 📌 Estructura del código

El archivo contiene:

### Clase: `Logic`

| Método              | Función                                                                 |
|---------------------|-------------------------------------------------------------------------|
| `__init__`           | Inicializa la expresión y prepara los contenedores                     |
| `funcionesFun()`     | Extrae los nombres de funciones usando expresiones regulares           |
| `constantesFun()`    | Detecta constantes numéricas en la expresión                           |
| `referenciasFun()`   | Identifica celdas individuales y rangos, evitando duplicación          |
| `imprimirCadenaFun()`| Muestra los resultados si la fórmula es válida                         |
| `clasificacionFun()` | Ejecuta el análisis completo si la cadena inicia con `=`               |

### Interfaz por consola

Un bucle `while` al final del archivo permite al usuario probar expresiones hasta ingresar una válida (que comience con `=`).

---

## ▶️ Cómo ejecutar

```bash
python logic_interpreter.py
