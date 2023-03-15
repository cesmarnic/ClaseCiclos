n = int(input("Ingrese el primer numero: "))
m = int(input("Ingrese el segundo numero: "))
suma = 0
if(n == m): print("Los numeros ingresados son iguales.")
else:
    for i in range(n, m+1):
        if(i % 2 == 0): suma += i

print("La suma de los numeros pares comprendidos desde",n,"hasta",m,"es: ",suma)
    