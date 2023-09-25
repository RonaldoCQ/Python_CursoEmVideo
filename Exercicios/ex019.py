from random import choice

alunos = [1,2,3,4]

print('Precisamos de 4 alunos candidatos para apagar o quadro. Pode escolher os nomes deles?')
for x in range(len(alunos)):
    alunos[x] = str(input('Digite o nome do {}º aluno candidato : '.format(x+1)))
    x = x+1

print('O aluno sorteado para apagar o quadro foi o {}. Boa sorte!'.format(choice(alunos)))