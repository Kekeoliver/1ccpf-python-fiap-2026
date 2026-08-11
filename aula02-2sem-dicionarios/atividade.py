eng2sp = dict()
print(eng2sp)

eng2sp  ['one'] = 'uno'
print(eng2sp)

eng2sp = {
    'one': 'uno',
    'two': 'dos',
    'three': 'tres'
}
print(eng2sp)
print(eng2sp['two'])

#OPERADOR IN
print('one' in eng2sp)

#VERIFICAR OS VALORES DO DICIONARIO
valores = eng2sp.values()
print('uno' in valores)


#DESAFIO CONTANTO LETRAS
def count_letters (s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

dict_contagem = count_letters('paralelepipedo')
print(dict_contagem)

#
