# test/test_logic.py
import pytest
import sys
import os
# Añadir al path el directorio src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from logic import Logic

def test_formula_valida():
    formula = "=SUMA(1, A1, B2:B5)"
    logica = Logic(formula)
    resultado = logica.clasificacionFun()
    
    assert resultado["constantes"] == [("1", "Evaluación directa")]
    assert resultado["referencias"] == [("A1", "Resolución de referencia")]
    assert resultado["rangos"] == [("B2:B5", "Resolución de referencia (rango)")]
    assert resultado["funciones"] == [("SUMA", "Evaluación funcional básica")]

def test_formula_funcion_desconocida():
    formula = "=FOO(2, B3)"
    logica = Logic(formula)
    with pytest.raises(ValueError, match="Función desconocida: FOO"):
        logica.clasificacionFun()

def test_formula_sin_igual():
    formula = "SUMA(1,2)"
    logica = Logic(formula)
    with pytest.raises(ValueError, match="La fórmula no comienza con '='"):
        logica.clasificacionFun()
