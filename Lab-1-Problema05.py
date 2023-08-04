def es_primo(n):
    cont = 0
    for k in range(1,n+1):
        if n%k == 0:
            cont += 1
    if cont == 2:
        return(True)
    else:
        return(False)

def lista_de_primos(n):
    primos = []
    for k in range(2,n+1):
        if es_primo(k) == True:
            primos.append(k)
    return(primos)

def find(array, len, summ):     #Funcion auxiliar que hace todas las sumas
    for i in range(len):
        for j in range(i, len):
            if (array[i] + array[j]) == summ:
                return(array[i], array[j])

def goldbach(n):
    primos = lista_de_primos(n)
    par = find(primos,len(primos),n)
    return par
    
a = int(input("Ingrese numero: "))
print(es_primo(a))              #Se verifica si es par o no
print(lista_de_primos(a))       #Lista de primos
print(goldbach(a))              #Se encuentra el par de primos que suma "a"
