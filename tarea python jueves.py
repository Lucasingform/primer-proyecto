print("seleccione el producto a canjear")
print("1- Gift card de $10.000, valor de 10.000 puntos")
print("2- secadora de pelo, valor de: 25.000 puntos")
print("3- disco duro portatil, valor de: 30.000 puntos")

print ("1. Ver mis puntos")
print ("2. Gastar mis puntos")
print ("3. salir")
op=int(input("seleccione una opcion: "))

puntos= 100000

continu = int(input("seleccione la opcion"))
if continu == 1:
    puntos = puntos-10000
    print(f"canje exitoso, le quedan: ${puntos} puntos")
if continu == 2:
    puntos = puntos-25000
    print(f"canje exitoso, le quedan: ${puntos} puntos")
if continu == 3:
    puntos = puntos-30000
    print(f"canje exitoso, le quedan: ${puntos} puntos")   
    
#Puntos acumulados
sw = 1
puntos = 100000
while sw==0:
    print("1. ver mis puntos")
    print("2. gastar mis puntos")
    print("3. salir")
    op=int(input("seleccione opcion: "))
    try:
     if(op > 0 and op < 4):
         if op == 1: 
            print(f"tiene un total de {puntos} puntos")
            continu = int(input("presione 1) para volver atras, presione 2) para salir"))
            if continu == 2:
                print("cierre de sesion exitoso, adios")
                sw = 0
         if op == 2:
          if (puntos>=10000):
              print("seleccione el producto a canjear")
              print("1- Gift card de $10.000, valor de 10.000 puntos")
              print("2- secadora de pelo, valor de: 25.000 puntos")
              print("3- disco duro portatil, valor de: 30.000 puntos")
              continu = int(input("seleccione la opcion"))
              if continu==1:
                  puntos = puntos-10000
                  print(f"canje exitoso, le quedan: ${puntos} puntos")
              if continu == 2:
                  puntos = puntos-25000
                  print(f"canje exitoso, le quedan: ${puntos} puntos")
              if continu == 3:
                  puntos = puntos-30000
                  print(f"canje exitoso, le quedan: ${puntos} puntos")
else:
    print("no le quedan puntos disponibles")
    if op == 3:
        print ("muchas gracias por utilizar el servicio, adios")
        sw=0
    else:
        print("seleccion fuera e rango")
         except:
        print("ingreso erroneo")                