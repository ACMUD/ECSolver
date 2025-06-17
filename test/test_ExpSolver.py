# test_exp_solver.py
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from exp_solver import ExpSolver, parsingExpresiones, evaluar_expresion

class TestExpSolver(unittest.TestCase):
    def setUp(self):
        self.solver = ExpSolver()
    
    # Tests existentes
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
    
    # Tests nuevos
    def testEvaluacionSimple(self):
        self.assertEqual(evaluar_expresion("SUMA(10, 5)"), 15)
        self.assertEqual(evaluar_expresion("RESTA(10, 5)"), 5)
    
    def testEvaluacionAnidada(self):
        self.assertEqual(evaluar_expresion("MAX(1, MIN(3, 4))"), 3)
        self.assertEqual(evaluar_expresion("SUMA(5, RESTA(10, 3))"), 12)
    
    def testFuncionDesconocida(self):
        with self.assertRaises(ValueError) as ctx:
            evaluar_expresion("DESCONOCIDA(1, 2)")
        self.assertIn("Función desconocida", str(ctx.exception))
    
    def testDivisionPorCero(self):
        with self.assertRaises(ValueError):
            evaluar_expresion("DIVIDIR(10, 0)")
    
    def testMultiplesFuncionesAnidadas(self):
        resultado = evaluar_expresion("SUMA(MAX(1, 2), MIN(3, 4), ABS(-5))")
        self.assertEqual(resultado, 10)  # 2 + 3 + 5

if __name__ == "__main__":
    unittest.main()