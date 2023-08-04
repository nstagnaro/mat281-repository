def divisores_propios(n):
    lista_divisores = []
    for k in range(1,n): #No consideramos el "n+1" para no ponerlo en la lista
        if n%k == 0:
            lista_divisores.append(k)
    return lista_divisores

def amigos(n,m):
    a = 0
    b = 0
    lista_1 = divisores_propios(n)
    lista_2 = divisores_propios(m)
    for k in lista_1:
        a += k
    if a != m:
        return(False)
    else:
        for k in lista_2:
            b += k
        if b == n:
            return(True)
        else:
            return(False)
    

a = int(input("Ingrese primer numero: "))
b = int(input("Ingrese segundo numero: "))
print(divisores_propios(a))     #Probando la funcion divisores propios
print(amigos(a,b))              #Probando la funcion amigos
