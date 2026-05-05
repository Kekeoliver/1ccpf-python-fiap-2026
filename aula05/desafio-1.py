pessoas = ['Leo', 'Ju', 'Caio', 'Anna']

for i in range(len(pessoas)):
    for j in range(i + 1, len(pessoas)):
        print(f"{pessoas[i]}, {pessoas[j]}")