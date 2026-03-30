dict_alunos1 = {'nome': 'Giovanna', 'situacao':'Matriculado','nota':'0'}
dict_alunos2 = {'nome': 'Gabriel Marques', 'situacao':'Evadido','nota':'0'}
dict_alunos3 = {'nome': 'Giovanna', 'situacao':'Matriculado','nota':'0'}

lista_aluno = [dict_alunos1, dict_alunos2, dict_alunos3]

for aluno in lista_aluno:
    if aluno["situacao"] != 'Matriculado':
        continue
    nota = float(input(f'Digite a nota do aluno {aluno['nome']}'))
    aluno ['nota'] = nota

    print(lista_aluno)