"""
Escribe un programa que pregunte al usuario si es culpable o no. Asumiremos que:

En caso afirmativo el usuario responderá si
En caso contrario responderá no.
Si el usuario responde si se imprimira «irás a la cárcel».

Si el usuario responde no se imprimira «irás a casa».

En cualquier caso se imprimira «la documentación por favor».
"""

afirmacion_del_usuario = input('Es usted culpable 😈 o inocente 😇, reponda con un Si o un No: ')

if afirmacion_del_usuario	== 'Si':
	print('Es culpable ⛓️')
elif afirmacion_del_usuario == 'No':
	print('Es inocente 🔑')
else:
	print('La documentacion por favor 🪪')
