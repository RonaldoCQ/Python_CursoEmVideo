from math import sqrt

n1 = int(input('Digite qualquer número: '))
dobro = n1*2
triplo = n1*3
raiz = sqrt(n1)

print('O número digitado foi: {} \nO seu dobro é {} \nO seu triplo é {} \nE sua raiz é {:.2f}'.format(n1,dobro,triplo,raiz))