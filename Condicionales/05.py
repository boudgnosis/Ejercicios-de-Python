""" Ejercicio
Escribir un programa que pida al usuario un número entero y muestre
por pantalla si es par o impar.
"""

# -- Solución --

numero = int(input('Por favor ingrese un número entero: '))

par_o_impar = numero % 2 

if par_o_impar == 0:
	print('Número par')
else:
  print('Número impar')
