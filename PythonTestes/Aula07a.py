#nome = str(input('Qual o seu nome?\n'))
#print('Prazer em te conhecer {:-^20}'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))

print('A soma vale {:^20.3F}'.format(n1+n2), end = "")
print('O produto vale {:^20}'.format(n1*n2), end = "")
print('A Divisão vale {:^20.3F}'.format(n1/n2))
