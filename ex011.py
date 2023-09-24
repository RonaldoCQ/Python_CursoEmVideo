#Faça um programa que leia a altura e largura de uma parede, calcule a sua área e a quantidade de tinta necessária para pinta-la.
#Cada litro de tinta pinta uma área de 2 metros

print('Bem-Vindo ao medidor de gasto de tinta por metro quadrado')
altura = int(input('Digite o valor (Em metros) da altura da parede que deseja pintar: '))
base = int(input('Digite o valor (Em metros) da largura da parede que deseja pintar: '))

area = base*altura

print('A área da sua parede é de {}, o que equivale a aproximadamente {} baldes de tinta.'.format(area,area/2))