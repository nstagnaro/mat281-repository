def factorial(n):
    if n == 0 or n == 1:
        resultado = 1
    else:
        resultado = n*factorial(n-1)
    return resultado

def suma(n):
    resultado = 0
    if n<0:
        print("Ingrese un valor valido por favor...")
    else:
        for k in range(0,n+1):
            resultado += 1/factorial(k)
    return resultado

a = int(input("Ingrese numero natural: "))
print(factorial(a))     #Probando el factorial
print(suma(a))          #Probando la suma
