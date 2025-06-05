import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from extension import FunctionRegistry


# --- Funciones de prueba ---
def suma(a, b):
    return a + b

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

if __name__ == "__main__":
    unittest.main()