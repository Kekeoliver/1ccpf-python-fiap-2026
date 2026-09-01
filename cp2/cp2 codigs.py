logs=(
("/login",200),
("/pedido",500),
("/login",401),
("/pedido",201),
("/login",200)
)

resultado ={}

for endpoint, codigo in logs:

    if endpoint not in resultado:
        resultado[endpoint]=[0, 0]

    resultado[endpoint][0]+=1

    if codigo >= 400:
        resultado[endpoint][1]+=1

print(resultado)








