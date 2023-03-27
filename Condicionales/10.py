"""
Escribe un programa que responda a un usuario que quiere comprar un helado en
una conocida marca de comida rápida cuanto le costará en función del topping
que elija.

En caso de no disponer del topping solicitado por el usuario el programa
escribirá por pantalla «no tenemos este topping, lo sentimos. » y a
ontinuación informar del precio del helado sin ningún topping.
Finalmente, el programa escribe por pantalla el precio del helado con el
topping seleccionado (o ninguno).
"""

# -- Solución --

helado_sin_topping = 1.90
topping_oreo = 1
topping_kitkat = 1.50
topping_brownie = 0.75
topping_lacasitos = 0.95

print(
	'Elija la opcion de topping que desea o si no lo quiere con topping:\n1. Oreo\n'
	'2. kitkat\n3. brownie\n4. locasitos\n5. sin topping')


eleccion_del_usuario = int(input('Por favor ingrese su elección: '))

if eleccion_del_usuario == 1:
	print(f'El costo del helado con topping de ore es de: {helado_sin_topping + topping_oreo}$')
elif eleccion_del_usuario == 2:
	print(f'El costo del helado con topping de kitkat es de: {helado_sin_topping + topping_kitkat}$')
elif eleccion_del_usuario == 3:
	print(f'El costo del helado con topping de brownie es de: {helado_sin_topping + topping_brownie}$')
elif eleccion_del_usuario == 4:
	print(f'El costo del helado con topping de locasitos es de: {helado_sin_topping + topping_lacasitos}$')
elif eleccion_del_usuario == 5:
	print(f'El costo del helado sin topping es de: {helado_sin_topping}$')
else:
	print(f'No tenemos ese topping, lo sentimos, el helado sin topping cuesta: {helado_sin_topping}')
