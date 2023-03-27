""" Ejercicio
pide al usuario que ingrese dos números y luego verifica cuál es el mayor.
"""

# -- Solución --

print('Por favor ingrese dos números')

n1 = int(input('Ingrese el primer número: '))
n2 = int(input('Ingrese el segundo número: '))

if n1 > n2:
	print('El primer número es mayor')
elif n2 > n1:
	print('El segundo número es mayor')
else:
	print('Los números son iguales')
