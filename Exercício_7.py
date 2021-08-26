#Exercício 7
#Igor Bragança - 01N11

'''Escreva um programa em Python que o usuário digita dois números inteiros e
armazena em duas variáveis n1 e n2, o seu programa deve trocar os valores
dessas variáveis, de maneira que o valor de n1 seja igual ao de n2 e
vice-versa, e depois deve exibir os números lidos com valores trocados'''

#Entrada
n1 = int(input("Digite o primeiro número"))
n2 = int(input("Digite o segundo número"))

#Processamento
n3 = n1
n1 = n2
n2 = n3

#Saída
print(f'n1={n1} e n2={n2}')
