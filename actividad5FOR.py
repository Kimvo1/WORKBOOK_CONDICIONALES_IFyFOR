palabras = ["hoja", "papel", "lapiz", "borrador"]

letra_inicial = input("Ingrese la letra inicial que desea buscar: ")


print(f"Palabras que comienzan con '{letra_inicial}':")
for palabra in palabras:
        if palabra.startswith(letra_inicial):
            print(palabra)

#Crear un programa que reciba una lista de palabras y muestre únicamente aquellas que empiezan con una letra 
# determinada, utilizando un ciclo for y una estructura condicional if