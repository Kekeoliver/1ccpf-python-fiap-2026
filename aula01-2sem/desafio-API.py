
endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]
print(endpoints[0])
print(status[0][2])

def eh_sucesso(codigo):
    return 200 <= codigo <= 299
print(eh_sucesso(status[2][1]))

def eh_erro(codigo):
    return 300 <= codigo <= 503
print(eh_erro(status[2][1]))





