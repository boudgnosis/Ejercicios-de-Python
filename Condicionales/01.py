""" Ejercicio
La jornada de trabajo es de 48 horas, calcular dada las horas trabajadas
con el valor por hora. Mostrar su salario e indicar las horas extras si
se excede de la jornada.
"""
#-- Solución --

jornada_de_trabajo = 48 # Esta en horas

horas_de_trabajo = int(input('Por favor ingrese las horas que trabajo: '))

pago_por_hora = float(input('Por favor indique cuanto es el pago por hora: '))

pago_horas_extra = float(input('Por favor ingrese cuanto es el pago por hora extra trabajada: '))

if jornada_de_trabajo == horas_de_trabajo:
  print(f'Su salario es de: {horas_de_trabajo * pago_por_hora}')
# Pregunto si la jornada laboral es menor a la que se trabajo y asi saco el total de horas extras trabajadas
elif jornada_de_trabajo < horas_de_trabajo:
  horas_extra_trabajada = -(jornada_de_trabajo - horas_de_trabajo)
  pago_por_horas_extras_trabajadas = horas_extra_trabajada * pago_horas_extra
  print(f'Su salario mas las horas extras trabajadas es de: {jornada_de_trabajo * pago_por_hora + pago_por_horas_extras_trabajadas}')
else:
  print('¿Es usted un esclavo?')
