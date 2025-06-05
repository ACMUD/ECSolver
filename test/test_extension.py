import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from extension import FunctionRegistry


# --- Funciones de prueba ---
def suma(a, b):
    return a + b

def error_func(a, b):
    return a / 0  # Genera error al evaluar


class TestFunctionRegistry(unittest.TestCase):

    def setUp(self):
        self.registry = FunctionRegistry()

    def registered_names(self):
        return [f["name"] for f in self.registry.get_registered_functions()]

    def test_register_success(self):
        self.registry.register("mi_suma", suma)
        self.assertIn("mi_suma", self.registered_names())

    def test_register_reserved_name(self):
        self.registry.register("SUM", suma)
        self.assertNotIn("SUM", self.registered_names())

    def test_register_non_function(self):
        self.registry.register("no_funcion", 123)
        self.assertNotIn("no_funcion", self.registered_names())

    def test_evaluate_success(self):
        self.registry.register("mi_suma", suma)
        resultado = self.registry.evaluate("mi_suma", 3, 4)
        self.assertEqual(resultado, 7)

    def test_evaluate_unregistered_function(self):
        resultado = self.registry.evaluate("desconocida", 1, 2)
        self.assertIsNone(resultado)

    def test_evaluate_function_with_error(self):
        self.registry.register("error_func", error_func)
        resultado = self.registry.evaluate("error_func", 1, 2)
        self.assertIsNone(resultado)

if __name__ == "__main__":
    unittest.main()