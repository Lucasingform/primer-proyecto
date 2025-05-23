
#menu de opciones

while True:
    print("Menu de opciones: ")
    print("1. SUMAR")
    print("2. MULTIPLICAR")
    print("3. DIVIDIR ")
    print("4. SALIR DEL PROGRAMA")
    op= input("ingrese su opcion: ")
    if op == 4:
        print("saliendo del programa")
        break
    elif op not in [1,2,3]:
        print ("opcion invalida. Por favor, intente nuevamente")
        continue
    
    cantidad_numeros = int(input("ingrese la cantidad de numeros: "))
    numeros = []
    for i un range (cantidad_numeros):
        numero = float(input(f"ingrese el numero{i+1}: "))
        numeros.append(numero)
        
        numero_operacion = float(input("ingrese el numero por el cual desea realizar la operacion: "))
        print ("lista original:")
        print (numeros)
        
        if op == 1 :
            resultados = [numero+numero_operacion for numero in numeros]
            print("resultados de la suma:")
