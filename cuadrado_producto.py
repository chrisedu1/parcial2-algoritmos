#Desarrollar un programa con dos funciones:
#La primera solicite el ingreso de un entero y muestre el cuadrado de dicho valor.
#La segunda que solicita la carga de dos valores y muestre el producto de los mismos.
#llamar desde el bloque principal a ambas funciones.

def cuadradonum(num):
    cuadrado = num ** 2
    print(f"El cuadrado de {num} es: {cuadrado}")

def producto_num(num1, num2):
    producto = num1 * num2
    print(f"El producto de {num1} y {num2} es: {producto}")

print("Calculamos el cuadrado de un numero entero.")
if __name__ == "__main__":
    numero_entero = int(input("Por favor, ingrese un número entero: "))

    cuadradonum(numero_entero)
    
    print("Calculamos el producto de dos numeros.")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    producto_num(num1, num2)
