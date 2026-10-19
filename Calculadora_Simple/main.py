# Calculadora Simple
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

resultado_suma = numero1 + numero2
print("La suma es:", resultado_suma)

# Retos extra
numero3 = float(input("Ingrese un tercer número: "))

resta = numero1 - numero2
multiplicacion = numero1 * numero2
modulo = numero1 % numero2
suma_tres = numero1 + numero2 + numero3

print("La resta es:", resta)
print("La multiplicación es:", multiplicacion)

if numero2 != 0:
    division = numero1 / numero2
    print("La división es:", division)
else:
    print("No se puede dividir entre cero.")

print("El módulo es:", modulo)
print("La suma de los tres números es:", suma_tres)