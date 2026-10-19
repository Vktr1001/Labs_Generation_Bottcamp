
#sumar(a, b): entra a y b → se suma a + b → se devuelve el resultado
#restar(a, b): entra a y b → se resta a - b → se devuelve el resultado
#multiplicar(a, b): entra a y b → se multiplica a * b → se devuelve el resultado
#dividir(a, b): entra a y b → se divide a / b → se devuelve el resultad
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir entre cero."
def modulo(a, b):
    if b != 0:
        return a % b
    else:
        return "No se puede calcular el módulo con divisor cero."
def potencia(a, b):
    return a ** b

if __name__ == "__main__":
# Pedimos los números al usuario
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    print("La suma es:", sumar(numero1, numero2))
    print("La resta es:", restar(numero1, numero2))
    print("La multiplicación es:", multiplicar(numero1, numero2))
    print("La división es:", dividir(numero1, numero2))
    print("El módulo es:", modulo(numero1, numero2))
    print("La potencia es:", potencia(numero1, numero2))
