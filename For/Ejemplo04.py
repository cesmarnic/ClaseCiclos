'''
    Factorial n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1
    5! = 5 * 4 * 3 * 2 * 1
    5! = 120

    7! = 7 * 6 * 5 * 4 * 3 * 2 * 1
    7! = 5040
'''
n = int(input("Ingrese el numero a calcular el factorial: "))
f = 1
for i in range(1, n+1):
    f *= i
print("El factorial de",n,"es",f)