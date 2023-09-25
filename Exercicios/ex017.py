#Receber o valor dos catetos Oposto e Adjacente, para calcular a hipotenusa
from math import hypot

oposto = input('Digite o valor do Cateto Oposto: ')

while oposto.isnumeric() == False:
    oposto = input('Por favor digite um valor numérico: ')
else:
    oposto = float(oposto)

adjacente = input('Digite o valor do Cateto Adjacente: ')

while adjacente.isnumeric() == False:
    adjacente = input('Por favor digite um valor numérico: ')
else:
    adjacente = float(adjacente)


#hipo = (oposto**2+adjacente**2)**(1/2)
hipo = hypot(oposto,adjacente)

print('O valor da hipotenusa desse triângulo é de: {:.2f}'.format(hipo))