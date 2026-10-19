from main import sumar, restar, multiplicar, dividir, modulo, potencia

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0

def test_restar():
    assert restar(5, 3) == 2
    assert restar(0, 5) == -5
    assert restar(-1, -1) == 0

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, 1) == -1
    assert multiplicar(0, 5) == 0

def test_dividir():
    assert dividir(6, 2) == 3
    assert dividir(0, 5) == 0
    assert dividir(5, 0) == "No se puede dividir entre cero."

def test_modulo():
    assert modulo(5, 2) == 1
    assert modulo(0, 5) == 0
    assert modulo(5, 0) == "No se puede calcular el módulo con divisor cero."

def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(-1, 2) == 1
    assert potencia(0, 5) == 0
