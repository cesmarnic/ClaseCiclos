# Numero Primo.
'''
    Todo numero primo es aquel numero que es
    divisible unicamente entre si mismo y la unidad.
    2 es primo, porque solo se puede dividir entre el mismo y 1
    3 es primo, porque solo se puede dividir entre 3 y 1
    4 no es primo, porque se puede dividir entre 4, 2 y 1
    5 es primo, porque solo se puede dividir entre 5 y 1
    6 no es primo, 6, 3, 2 y 1.
'''
print("Programa para indicar si un numero es primo.")
n = int(input("ingrese un numero: "))
c = 0

for i in range(1, n+1):
    if(n % i == 0):
        c += 1

if(c == 2):
    print(n,"es un numero primo")
else:
    print(n,"no es un numero primo")