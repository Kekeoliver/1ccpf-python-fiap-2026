temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

maior_contagem = -1
sala_recordista = 0

for i, sala in enumerate(temperaturas):
    # print(sala)
    contagem = 0
    media = 0
    for temp in sala:
        if temp >= 33:
            contagem = contagem + 1
        # print(temp)
        media = media + temp

    if contagem > maior_contagem:
        maior_contagem = contagem
        sala_recordista = i+1

    print(f"Sala {i+1}")
    print(media/4)
    print (contagem)
    print()


print(f"A sala com maior quantidade de registros criticos foi: {sala_recordista} com {maior_contagem} registros")