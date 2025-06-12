from ECSolver.src.basic import ExcelCalculadora

################################ PRUEBAS DE USO ################################

def probar_calculadora():
    calc = ExcelCalculadora()

    print("--- CASOS DE PRUEBA ---\n")

    def test_suma():
        calc = ExcelCalculadora()
        resultado = calc.suma(1, 2, 3)
        print("Resultado de suma:", resultado)
        assert resultado == 6

    def test_promedio():
        calc = ExcelCalculadora()
        resultado = calc.promedio(2, 4, 6)
        print("Resultado de promedio:", resultado)
        assert resultado == 4.0

    def test_maximo():
        calc = ExcelCalculadora()
        resultado = calc.maximo(10, 50, 20)
        print("Resultado de maximo:", resultado)
        assert resultado == 50

    def test_minimo():
        calc = ExcelCalculadora()
        resultado = calc.minimo(5, 3, 9)
        print("Resultado de minimo:", resultado)
        assert resultado == 3

    def test_multiplicar():
        calc = ExcelCalculadora()
        resultado = calc.multiplicar(2, 3, 4)
        print("Resultado de multiplicar:", resultado)
        assert resultado == 24

    def test_dividir():
        calc = ExcelCalculadora()
        resultado = calc.dividir(10, 2)
        print("Resultado de dividir:", resultado)
        assert resultado == 5.0

    def test_resta():
        calc = ExcelCalculadora()
        resultado = calc.resta(10, 2, 3)
        print("Resultado de resta:", resultado)
        assert resultado == 5

    def test_potencia():
        calc = ExcelCalculadora()
        resultado = calc.potencia(2, 3)
        print("Resultado de potencia:", resultado)
        assert resultado == 8

    def test_raiz():
        calc = ExcelCalculadora()
        resultado1 = calc.raiz(9)
        resultado2 = calc.raiz(8, 3)
        print("Resultado de raiz(9):", resultado1)
        print("Resultado de raiz(8, 3):", resultado2)
        assert resultado1 == 3
        assert resultado2 == 2

    def test_si():
        calc = ExcelCalculadora()
        resultado1 = calc.si(True, "ok", "fail")
        resultado2 = calc.si(False, "ok", "fail")
        print("Resultado de si(True, 'ok', 'fail'):", resultado1)
        print("Resultado de si(False, 'ok', 'fail'):", resultado2)
        assert resultado1 == "ok"
        assert resultado2 == "fail"

    def test_y():
        calc = ExcelCalculadora()
        resultado1 = calc.y(True, True, True)
        resultado2 = calc.y(True, False, True)
        print("Resultado de y(True, True, True):", resultado1)
        print("Resultado de y(True, False, True):", resultado2)
        assert resultado1 is True
        assert resultado2 is False

    def test_o():
        calc = ExcelCalculadora()
        resultado1 = calc.o(False, False, True)
        resultado2 = calc.o(False, False, False)
        print("Resultado de o(False, False, True):", resultado1)
        print("Resultado de o(False, False, False):", resultado2)
        assert resultado1 is True
        assert resultado2 is False

    #Función contar
    def test_contar():
        assert calc.CONTAR(1, 2.5, "texto", None) == 2

    #Función contará
    def test_contara():
        assert calc.CONTARA(1, "", None, "hola", 0) == 4

    #Función contar si
    def test_contar_si():
        assert calc.CONTAR_SI([1, 2, 3, 4], lambda x: x > 2) == 2

    #Función buscarv
    def test_buscarv():
        tabla = [["Ana", 30], ["Luis", 25]]
        assert calc.BUSCARV("Luis", tabla, 1) == 25

    #Función buscarh
    def test_buscarh():
        tabla = [["Nombre", "Edad"], ["Ana", 30]]
        assert calc.BUSCARH("Edad", tabla, 1) == 30

    #Función concatenar
    def test_concatenar():
        assert calc.CONCATENAR("Hola", " ", "mundo", "!") == "Hola mundo!"


    def test_concat():
        calc = ExcelCalculadora()
        resultado = calc.concat("Hola", " ", "mundo")
        print("Resultado de concat:", resultado)
        assert resultado == "Hola mundo"

    def test_izquierda():
        calc = ExcelCalculadora()
        resultado = calc.izquierda("Python", 2)
        print("Resultado de izquierda:", resultado)
        assert resultado == "Py"

    def test_derecha():
        calc = ExcelCalculadora()
        resultado = calc.derecha("Python", 3)
        print("Resultado de derecha:", resultado)
        assert resultado == "hon"

    def test_largo():
        calc = ExcelCalculadora()
        resultado = calc.largo("Python")
        print("Resultado de largo:", resultado)
        assert resultado == 6

    def test_ahora():
        calc = ExcelCalculadora()
        resultado = calc.ahora()
        print("Resultado de ahora:", resultado)
        assert isinstance(resultado, str)

    def test_hoy():
        calc = ExcelCalculadora()
        resultado = calc.hoy()
        print("Resultado de hoy:", resultado)
        assert isinstance(resultado, str)