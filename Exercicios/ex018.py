#Calcular os valores de um ângulo dado pelo usuário
from math import sin,cos,tan,radians

ang = int(input('Digite o valor do Ângulo que deseja: '))

ang = radians(ang)

print('Os valores dos ângulos são: \n{:.2f} para o Seno\n{:.2f} para o Cosseno\n{:.2f} para a Tangente'.format(sin(ang),cos(ang),tan(ang)))

