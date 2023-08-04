def suma(n):
    resultado = 0
    if n<0:
        print("Numero no valido, ingrese de nuevo por favor...")
    else:
        for k in range(1,n+1): #hasta n+1 para que tome el termino n
            resultado += 4*(((-1)**(k+1))/(2*k-1)) 
        return resultado

n = int(input("Indique cuantos terminos de la suma usara: "))
print(suma(n))
