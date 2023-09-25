#Sortear os alunos igual ao exercicio anterior só que agora mostrando os nomes e ordem
from random import shuffle

nomes = [1,2,3,4]

for x in range(len(nomes)):
    nomes[x] = input('Digite o nome do aluno para ser sorteado: \n')
    while nomes[x].isalpha() == False:
        print('Erro! O valor digitado não é um nome. Por favor, digite apenas nomes')
        nomes[x] = input('Digite um nome válido: \n')

    else:
        x = x+1

for x in range(len(nomes)):
    shuffle(x=nomes)
    x = x+1
print('A sequencia de apresentações será: {}'.format(nomes))