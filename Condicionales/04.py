""" Ejercicio
Escribir un programa que pida al usuario dos números y muestre por
pantalla su división. Si el divisor es cero el programa debe mostrar
un error.
"""

# -- Solución --

print('Acontinuación se le pediran dos números')

numero_uno = float(input('Por favor ingrese un número: '))
numero_dos = float(input('Por favor ingrese el segundo número: '))

if numero_uno == 0:
	print('❌ERROR❌, no se puede dividir por cero porque el resultado siempre es cero.')
elif numero_dos == 0:
	print('❌ERROR❌, no se puede dividir por cero porque el resultado siempre es cero.')
else:
  print(f'La división da como resultado: {numero_uno / numero_dos}.')


