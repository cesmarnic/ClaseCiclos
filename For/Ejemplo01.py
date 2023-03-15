# Fizz Buzz
'''
    Recorrer los numeros del 1 al 100.
    Si el numero es un multiplo de 3, mostrar la palabra Fizz
    Si el numero es un multiplo de 5, mostrar la palabra Buzz
    Si el numero es multilpo de 3 y de 5 al mismo tiempo, mostrar FizzBuzz
'''

for n in range(1, 101):
    if(n % 5 == n % 3 == 0):
        print("FizzBuzz")
    elif(n % 3 == 0):
        print("Fizz")
    elif(n % 5 == 0):
        print("Buzz")
    else:
        print(n)