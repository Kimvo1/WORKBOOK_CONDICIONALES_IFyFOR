lista1 = input("Ingrese la primera lista de números separados por comas: ")
lista2 = input("Ingrese la segunda lista de números separados por comas: ")
lista1 = lista1.split(",")
lista2 = lista2.split(",")
lista_suma = []
for i in range(len(lista1)):
    suma = int(lista1[i]) + int(lista2[i])
    lista_suma.append(suma)
(print(lista_suma))
    
    
#Crear un programa que reciba dos listas de números y que genere una tercera lista que contenga la suma de los elementos de las dos listas en la misma posición, utilizando un ciclo for  
                