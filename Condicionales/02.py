""" Ejercicio
Escribir un programa que pregunte al usuario su edad y muestre por
pantalla si es mayor de edad o no.
"""

# -- Solución --

edad = int(input('Por favor ingrese su edad: '))

if edad >= 18 | edad <= 119:
  print('Es usted mayor de edad.')
elif edad >= 120:
  print('¿Me esta mintiendo 🤨?')
elif edad <= 0:
  print('No mienta por favor 🫤.')
else:
  print('Usted no es mayor de edad.')
