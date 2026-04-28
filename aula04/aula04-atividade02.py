def verificar_nota(nota):
    while nota < 0 and nota > 10:
        print("A nota deve estar entre 0 e 10")
        notaA = float(input("Digite sua nota novamente:"))
    return nota



notaA = float(input("Digite a primeira nota: "))
notaA = verificar_nota (notaA)


notaB = float(input( "Digite a segunda nota: "))
notaB = verificar_nota(notaB)


media = (notaA + notaB) / 2
print(media)
