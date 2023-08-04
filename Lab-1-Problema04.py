def collatz(n):
    secuencia = []
    secuencia.append(n)
    while n != 1:
        if n%2 != 0:   #Caso impar
            n = 3*n + 1
            n = int(n)
            secuencia.append(n)
        elif n%2 == 0: #Caso par
            n = n/2
            n = int(n)
            secuencia.append(n)
    return secuencia

a = int(input("Ingrese numero entero positivo: "))
print(collatz(a))
        
        
#los int(n) es porque me quedaban floats al operar n en los casos.
