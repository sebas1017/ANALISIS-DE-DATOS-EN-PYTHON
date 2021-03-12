import csv
import matplotlib.pyplot as plt
import funciones
from pprint import pprint
import collections
fecha_nacimiento_hombres = list()
separados = list()
correos = list()
religiones = list()
fecha_nacimiento_mujeres = list()
paises_personas_totales = list()
edades_finales_hombres = list()
edades_finales_mujeres = list()
paises = list()
dominios  = list()
meses_nacimiento_hombres = list()
meses_nacimiento_mujeres= list()
grupo_sanguineo_hombres=list()
#leemos los datos del csv y los clasificamos en listas para luego 
#convertir esos datos en informacion
with open("personas.csv")as archivo:
  fuente = csv.reader(archivo, delimiter="|")
  for linea in fuente:
    if "M" in linea[3]:
      fecha_nacimiento_hombres.append(linea[4])
      grupo_sanguineo_hombres.append(linea[7])
    if "F" in linea[3]:
      fecha_nacimiento_mujeres.append(linea[4])  
    paises_personas_totales.append(linea[11])
    religiones.append(linea[13])
    correos.append(linea[12])
    
funciones.calcularFecha(fecha_nacimiento_hombres,edades_finales_hombres)
funciones.calcularFecha(fecha_nacimiento_mujeres,edades_finales_mujeres)

print(20*"*-*")
print("PUNTO 1 DESARROLLADO")
print("el promedio de edad de los hombres es:"+str(funciones.promedioPersonas(edades_finales_hombres)))
print("el promedio de edad de las mujeres es:"+str(funciones.promedioPersonas(edades_finales_mujeres)))


print(20*"*-*")
print("PUNTO 2 DESARROLLADO")
lista2 = (religiones)
# Crear un objeto Counter a partir de la lista lista1
repetidos1 = collections.Counter(lista2)
del repetidos1["religion"]
print("EL PORCENTAJE DE PERSONAS  POR CADA RELIGION  ES: ")
for llave, valor in repetidos1.items():
  print(llave,str((int(valor)*100)/10000)+"%"+" "+ "personas")


print(20*"*-*")
print("PUNTO 3 DESARROLADO")
for p in range(len(correos)):
  cadena = str()
  cadena = (str(correos[p]))
  str(cadena)
  necesaria = cadena.find("@")
  dominios.append(cadena[necesaria:])
  cadena = str()
lista7 = (dominios)
repetidos8 = collections.Counter(lista7)
del repetidos8["correo"]
del repetidos8["o"]
lista=[]
for i in repetidos8:
    lista.append(repetidos8[i])
inverse = [(value, key) for key, value in repetidos8.items()]
print ("EL DOMINIO DE CORREO MAS COMUN ES:"+max(inverse)[1]+" "+"Y SU FRECUENCIA DE REPETICION ES :"+str(max(lista)))
print(20*"*-*")


print("PUNTO 4 DESARROLLADO")
lista1 = (paises_personas_totales)
# Crear un objeto Counter a partir de la lista lista1
repetidos = collections.Counter(lista1)
del repetidos["pais"]
# En el objeto Counter las llaves son los 
# elementos (sin repetir) de la lista paises y los valores el
# número de veces que aparece cada elemento en la lista.
print("EL NUMERO DE PERSONAS POR CADA PAIS ES: ")
for llave, valor in repetidos.items():
  print(llave,str(int(valor))+" "+"personas")
  

print("PUNTO 5 DESARROLLADO")
funciones.calcularMeses(fecha_nacimiento_hombres,meses_nacimiento_hombres)
funciones.calcularMeses(fecha_nacimiento_mujeres,meses_nacimiento_mujeres)

lista01= []
lista02= []
lista03 = []
lista9 = (meses_nacimiento_hombres)
lista10 =(meses_nacimiento_mujeres)
# Crear un objeto Counter a partir de la lista lista1
repetidos0 = collections.Counter(lista9)
repetidos03 = collections.Counter(lista10)

funciones.repetidos(lista01,repetidos0,"maximo_meses_nacimiento_hombres")
funciones.repetidos(lista02,repetidos0,"minimo_meses_nacimiento_hombres")



print(20*"*-*")
print("PUNTO 6 DESARROLLADO")
lista07 = (meses_nacimiento_mujeres)
repetidos = collections.Counter(lista07)
pprint(repetidos)
print("EL PORCENTAJE DE MUJERES  POR CADA MES  ES: ")
for llave, valor in repetidos.items():
  print(llave,str(valor*100/10000)+"%"+" "+ "MUJERES")

plt.bar(*zip(*repetidos.items()))
plt.show()  
print(20*"*-*")
print(20*"*-*")
print("PUNTO 7 DESARROLLADO")
lista04= (grupo_sanguineo_hombres)
# Crear un objeto Counter a partir de la lista lista1
repetidos1 = collections.Counter(lista04)

print("Imprimiendo rpeetidos ")
print(repetidos1)
print("EL PORCENTAJE DE HOMBRES POR CADA GRUPO SANGUINEO  ES: ")
for llave, valor in repetidos1.items():
  print(llave,str((int(valor)*100)/10000)+"%"+" "+ "HOMBRES")



