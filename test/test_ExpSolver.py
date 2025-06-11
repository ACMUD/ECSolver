import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from exp_solver import parsingExpresiones


class TestParser(unittest.TestCase):
    def testSimple(self):
        funcion, argumentos = parsingExpresiones("SUMA(10,5)")
        self.assertEqual(funcion, "SUMA")
        self.assertEqual(argumentos, ["10","5"])

    def testAnidadas(self):
        funcion, argumentos = parsingExpresiones("MAX(1, MIN(3,4))")
        self.assertEqual(funcion, "MAX")
        self.assertEqual(argumentos, ["1","MIN(3,4)"])

    def testExpresionInvalida(self):
        with self.assertRaises(ValueError):
            parsingExpresiones("INVALIDA 0, 8")

if __name__ == "__main__":
    unittest.main()
