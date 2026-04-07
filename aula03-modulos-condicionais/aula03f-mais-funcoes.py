def boas_vindas(nome):
    print(f"Olá, {nome}! Seja bem-vindo!")

nome_digitado = input("Digite seu nome: ")
boas_vindas(nome_digitado)

#FUNÇÃO COM PARAMETRO DE RETORNO
def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

resultado = soma(4, 3)
print(soma(4 , 3 ))
print(type(nome_digitado))
