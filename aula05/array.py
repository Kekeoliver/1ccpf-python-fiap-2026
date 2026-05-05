lista_frutas = ["Uva", "Banana", "Melancia"]
print(lista_frutas)

lista_frutas.append("pitaya") # adiciona no final da lista
print(lista_frutas)

for i in range(len(lista_frutas)): # len = calcula o tamanho da lista
    print(lista_frutas[i])

for fruta in lista_frutas:
    print(fruta)
    