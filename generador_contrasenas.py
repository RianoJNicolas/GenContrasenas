import random

def generar_contrasena():
    mayus = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q']
    minus = ['a','b','c','d','e','f','g','h']
    simbolos = ['!','#','$','%','&','/','(',')']
    numeros = ['1','2','3','4','5','6','7','8','9']

    caracteres = mayus + minus + simbolos + numeros

    contrasena =[]

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    
    res = ''
    for char in contrasena:
        res = res + char
    
    return res

def main():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)


if __name__ == '__main__':
    main()