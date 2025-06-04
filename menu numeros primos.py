rangocreado=False
inicioR=0
finRango=0
while True:
    print("*** Generador de numeros Primos en Rango ***")
    print("1,- INGRESA EL RANGO DE NUMEROS ")
    print("2,- GENERAR NUMEROS PRIMOS ")
    print("3,- SALIR")
   
    opcmenu=0
   
    try:
        opcmenu= int(input("ingrese su opcion entre 1 y 3: "))
        if opcmenu==1:
            while True:
                try:
                    inicioR= int(input("ingrese inicio de Rango: "))
                    finRango=int(input("ingrese Fin de Rango: "))
                    if inicioR<finRango:
                        rangocreado=True
                        break
                    else:
                        print("El inicio debe ser menor que el fin del Rango")
                except:
                    print ("los numeros ingresados deben ser enteros")
        elif opcmenu ==2:     
           if rangocreado:
            for numero in range(inicioR, finRango+1):
                if numero==2:
                    print (f"{numero} es primo")      
                else:
                    if numero>2:
                        primo=True    
                        for i in range(2,numero):
                            if numero%i==0:
                                primo=False
                                break
                        if primo:
                            print (f"{numero} es primo")
            tecla=input("presione cualquier Tecla para continuar")               
           else:
               print("no se ha ingresado el rango")
               continue
        elif opcmenu== 3:
         print("Esta saliendo del programa, Adios!!")
         break
        else: 
            print("la opcion ingresada no es valida, debe ser entre 1 y 3")
    except:
        print ("debe ingresar un numero entero")
                             
    
    
    
    
