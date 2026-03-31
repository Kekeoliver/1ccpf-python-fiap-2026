#LOGICA E (AND)

verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)

#LOGICA OU (OR)

logica_ou = False or False or False
print(logica_ou)

# NOT

negacao = not False
print(negacao)

if not verifica_login:
    print("Errado")
else:
    print("Entra")

