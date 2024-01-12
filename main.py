try:
    numero = int(input('Ingrese un numero: '))
    resultado = 50 // numero
    print(f'50 // {numero} = {resultado}')
except ValueError:
    print('Error: ingresaste texto, pero debes ingresar numeros.')