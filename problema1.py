def sumar_5_enteros():
    #Definir variables a usar
    lista=[]
    contradormientras=0
    tamano=5
    suma=0


    #ingrese los numeros
    while contradormientras<tamano:
        lista.append(int(input("ingrese numero "+ str(contradormientras+1)+ ":")))
        contradormientras+=1

    contradormientras=0
    while contradormientras<tamano:
        suma +=lista[contradormientras]
        contradormientras+=1

    print("Los numeros de la lista son: ")
    for numero in lista:
        print(numero,end=',')

    print("\nla suma de todos sus elementos es:")
    print(suma)
