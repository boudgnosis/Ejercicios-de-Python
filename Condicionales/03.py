""" Ejercicio
Escribir un programa que almacene una contraseña
en una variable, pregunte al usuario por la contraseña e imprima por
pantalla si la contraseña introducida por el usuario coincide con la
guardada en la variable o no
"""

# -- Solución --

contraseña_bd = 'miEdadDeNascimento'

contraseña_usuario = input('Por favor ingrese su contraseña: ')

if contraseña_bd == contraseña_usuario:
	print('Su contraseña es correcta 😀.')
else:
  print('Contraseña incorrecta 😣.')
