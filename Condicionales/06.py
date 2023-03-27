"""Ejercicio
Pide al usuario que ingrese un número y luego verifica si es positivo, negativo
o cero.
"""

# -- Solución --

numero_usuario = int(input(
    'Por favor ingrese un número para verificar si es negativos, positivo o cero: '))

if numero_usuario < 0:
    print('Es negativo')
elif numero_usuario > 0:
    print('Es positivo')
else:
    print('Es cero')
