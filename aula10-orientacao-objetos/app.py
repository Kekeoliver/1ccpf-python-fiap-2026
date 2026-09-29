from aluno import Aluno
from disciplina import Disciplina

nome_aluno = "Keke"

# CRIAR / INSTANCIAR 1 Aluno
aluno1 = Aluno("Joao", "123456", "Ciência da computação")

# CRIAR / INSTANCIAR 2 DISCIPLINAS
prompt_ia = Disciplina("Prompt IA", "Jorge")
sers = Disciplina("SERS", "Andre")

# MATRICULAR O ALUNO NAS DISCIPLINAS
aluno1.matricula(prompt_ia)
aluno1.matricula(sers)
#print(aluno1.disciplinas[0].professor)


# ADICIONAR NOTA DO ALUNO REFERENTE ÁS DISCIPLINAS
aluno1.adicionar_nota(prompt_ia,10 )
aluno1.adicionar_nota(prompt_ia, 8)
aluno1.adicionar_nota(sers, 5)
aluno1.adicionar_nota(sers, 4)

print(aluno1.calcular_media_d(sers))
print(aluno1.calcular_media_geral())