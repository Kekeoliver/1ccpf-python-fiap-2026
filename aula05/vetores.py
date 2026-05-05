texto = "FIAP paulista"
print(texto)
print(texto[0])

tamanho = len(texto) # tamanho da string
print(tamanho)
print()

for i in range(tamanho):
   # print(texto [i]) # printa todos os elementos, apenas o "i" printa apenas os numeros de elementos
    print(f"texto[{i}] = {texto[i]}")

for c in texto:
    print(c) # c = caractere