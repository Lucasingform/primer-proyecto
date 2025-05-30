#calculadora simple
print ("calculadora simple")
print ("1, sumar(+)")
print ("2, restar(-)")
print ("3, multiplicar(*)")
print ("4, dividir(/)")
print ("5, salir")

while True:
    try: 
        opcion=int(input("seleccione la opcion deseada(1-5"))
        if opcion < 1 or opcion > 5:
            print("opcion invalida por favor ingrese otro numero valido (1-5)")
            continue
        break
    except ValueError:
        print("entrada invalida, por favor ingrese un numero: ")

try:
    num1 = float(input("ingrese el primer numero: "))
    num2 = float(input("ingrese el segundo numero: "))
except ValueError:
    print("entrada invalida, por favor ingrese un numero: ")
    return

if opcion == 1:
    resultado= num1+num2
    print (f"la suma de {num1} y {num2} da como resultado: {resultado}")