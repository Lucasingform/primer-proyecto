12
#tarea 1 bultos
CantidadBultos = 0
tieneMasBultos = True
nroBulto = 1
ValorPesoLiviano = 1000
ValorPesoNormal = 2000
TotalLivianos = 0
TotalNormales = 0
ContadorBultosLivianos = 0
ContadorBultosNormales = 0

CantidadBultos = int(input("ingrese cantidad de bultos que desea llevar:"))
for i in range(CantidadBultos):
    try:
      pesoBulto = int(input("ingrese el peso del bulto (1 a 10kg) del bulto {nroBulto}: "))
    except ValueError:
      print ("peso del bulto debe estar en el rango de 1 y 10kg")
      continue

if 5>= pesoBulto:
    TotalLivianos += ValorPesoLiviano
    ContadorBultosLivianos += 1
elif 10> pesoBulto:
    TotalNormales += ValorPesoNormal
    ContadorBultosNormales += 1
else:
    print ("Peso ingresado incorrecto (1-10kg)")
    nroBulto += 1
  
print(f"Total a pagar por los bultos livianos: {TotalLivianos}")
print (f"total a pagar por bultos normales: {TotalNormales}")
print (f"cantidad de bultos livianos: {ContadorBultosLivianos}")
print (f"cantidad de bultos normales: {ContadorBultosNormales}")
print (f"total a pagar por todos los bultos es: {TotalLivianos+TotalNormales}")