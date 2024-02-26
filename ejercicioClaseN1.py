def calculadora(operacion, num1, num2):
    suma = 0
    producto = 0

    if operacion == 1:
        suma = num1 + num2
        return suma
    else:
        resta = num1 - num2
        return resta
    
n1 = int(input('Ingrese el primer número: '))
n2 = int(input('Ingrese el segundo número: '))
op = input('Ingrese 1 para sumar o 2 para restar: ')

resultado = calculadora(op, n1, n2)

print('\El resultado de la operación es: ', resultado)