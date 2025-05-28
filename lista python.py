lista=[]
while True:
    print("Menú de opciones:")
    print("1. Insertar al final de la lista")
    print("2. Insertar en posición específica")
    print("3. Eliminar de la lista")
    print("4. Invertir lista")
    print("5. Ordenar lista")
    print("6. Salir")

    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        elemento = input("Ingrese el elemento a insertar: ")
        lista.append(elemento)
        print(f"Elemento '{elemento}' insertado al final de la lista.")
    elif opcion == "2":
        elemento = input("Ingrese el elemento a insertar: ")
        posicion = int(input("Ingrese la posición específica: "))
        if posicion <= len(lista):
            lista.insert(posicion - 1, elemento)
            print(f"Elemento '{elemento}' insertado en la posición {posicion}.")
        else:
            print("Posición inválida.")
    elif opcion == "3":
        if lista:
            elemento = input("Ingrese el elemento a eliminar: ")
            if elemento in lista:
                lista.remove(elemento)
                print(f"Elemento '{elemento}' eliminado de la lista.")
            else:
                print("Elemento no encontrado en la lista.")
        else:
            print("La lista está vacía.")
    elif opcion == "4":
        if lista:
            lista.reverse()
            print("Lista invertida.")
        else:
            print("La lista está vacía.")
    elif opcion == "5":
        if lista:
            lista.sort()
            print("Lista ordenada.")
        else:
            print("La lista está vacía.")
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, intente nuevamente.")

    print(f"Lista actual: {lista}")