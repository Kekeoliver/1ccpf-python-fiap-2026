
endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]
print(endpoints[0])
print(status[0][2])

#Função para detectar se UM status é sucesso

def eh_sucesso(codigo):
    return 200 <= codigo <= 299

# print(eh_sucesso(status(200)))

#Função que valida na lista de rq DE UM edpoint SE tem DOIS erros seguidos

def erros_seguidos(respostas_http):
    for i in range(len(respostas_http) - 1 ):
        codigo_atual = respostas_http[i]
        prox_codigo = respostas_http[i + 1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False
def analizar_endpoint(respostas_http):
    qnt_sucesso = 0

    for cod_http in respostas_http:
        if eh_sucesso(cod_http):
            qnt_sucesso += 1

    qnt_tot_req = len(respostas_http)
    qnt_erros = qnt_sucesso - qnt_tot_req

    percentual_sucessos = (qnt_sucesso / qnt_tot_req) * 100

    tem_erros_seguidos = erros_seguidos(respostas_http)

    if tem_erros_seguidos:
        classificacao = 'CRÍTICO'
    elif percentual_sucessos > 80:
        classificacao = 'ESTÁVEL'
    else:
        classificacao = 'INSTÁVEL'

    return (classificacao, qnt_sucesso, qnt_erros , percentual_sucessos)


#PERCORRENDO TODA A MATRIZ
maior_qnt_erros = -1
edpoint_maior_erro =''

# PERCORRENDO TODA A MATRIZ
for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    respostas_endpoint = status[i]

    sucesso, erros, percentual, classificacao = analizar_endpoint(respostas_endpoint)

    print(f'endpoint: {nome_endpoint}')
    print(f'resposta http: {respostas_endpoint}')
    print(f'sucessos: {sucesso}')
    print(f'erros: {erros}')
    print(f'percentual sucessos: {percentual}')
    print('-' * 30)
    print()

    if erros > maior_qnt_erros:
        maior_qnt_erros = erros
        edpoint_maior_erro = nome_endpoint


print(f'edpoint com mais erros : {edpoint_maior_erro}({maior_qnt_erros}')







