from datetime import datetime

def promedioPersonas(edades1):
  promedio = sum(edades1)/len(edades1)
  return promedio  


def calcularFecha(edadesh,edades_calculadas):
    #para calcular edades a partir de las fechas de nacimiento lo hacemos
    #de esta forma , considerando años bisiestos para mayor exactitud ...
  for i in range(len(edadesh)):
    b= (edadesh[i])
    formato_fecha = "%Y-%m-%d"
    fecha = datetime.today()
    fecha_actual= fecha.strftime(formato_fecha)
    fecha_inicial = datetime.strptime(str(b),formato_fecha)
    fecha_final = datetime.strptime(fecha_actual, formato_fecha)
    diferencia = fecha_final - fecha_inicial
    x = int()
    x = diferencia.days
    x = int(x/365)
    edades_calculadas.append(x)
    x= 0
    b = 0

def calcularMeses(edades_personas,meses_personas):
  for m in range(len(edades_personas)):
    cadena = str()
    cadena = (str(edades_personas[m]))
    necesaria = cadena.find("-")
    meses_personas.append(cadena[necesaria+1:7])  

def repetidos(meses_nacimiento,repetidos,sexo):
    for i in repetidos:
      meses_nacimiento.append(repetidos[i])
    inverse = [(value, key) for key, value in repetidos.items()]
    if sexo == 'maximo_meses_nacimiento_hombres':
        print ("EL MES EN QUE MAS NACIERON HOMBRES ES:"+max(inverse)[1]+" "+"Y EL NUMERO DE HOMBRES QUE NACIERON ESE MES ES :"+str(max(meses_nacimiento)))
    if sexo == 'minimo_meses_nacimiento_hombres':
      print ("EL MES EN QUE MENOS NACIERON HOMBRES ES:"+min(inverse)[1]+" "+"Y EL NUMERO DE HOMBRES QUE NACIERON ESE MES ES :"+str(min(meses_nacimiento)))