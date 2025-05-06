#solicitar datos al usuario 
quintil = int(input("ingrese su quintil (1-5): "))
condicion = input ("ingrese su condicion laboral (empleado/desempleado): ").strip().lower()
edad = int(input("ingrese su edad: "))

#determinar el subsidio base segun quintil y condicion laboral 
if quintil in [1, 2]:
    if condicion == "desempleado":
        subsidio = 10000
    else:
        subsidio =8000
elif quintil == 3:
        if condicion == "desempleado":
        subsidio = 6000
else:
    subsidio =4000
elif quintil in [4, 5]:
    subsidio = 1500
    else:
        subsidio = 0 #si el quintil ingresado es invalido
        
        #aplicar bonos adicionales
        if quintil in [1, 2]: 
            subsidio += 2000
            if quintil [1, 2] and edad > 65:
                subsidio += 3000
                #mostrar resultado
                print (f"El valor del subsidio de gas es: ${subsidio:,}".replace(",", "."))