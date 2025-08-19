#Recuperação de POO
#Questão 1
#Escreva um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso
#o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
    nota_str = input("Informe uma nota:")
    if nota_str.isdigit(): #isdigit() usada para verificar se todos 
        #os caracteres de uma string são dígitos numéricos
        # (não reconhece sinais de ponto decimal ou negativos) 
        nota_int = int(nota_str)
        if 0 <= nota_int <= 10:
            print(f"O valor {nota_int} é válido!")
            break
        else:
            print("Valor inválido, tente novamente...")    
    else:
        print("Valor inválido, tente novamente...")

#Questão 2
#Podemos usar isso:
# maior = -1000 onde o número que o usuário digitar pode ser maior que -1000
# menor = 1000 onde o número que o usuário digitar pode ser menor que 1000
#Porém o pyhton tem a função float('-inf') (infinito negativo) e float ('inf') (infinito positivo):
maior = float('-inf')
menor = float('inf')

while True:
    valor_str = input("Informe um valor inteiro (ZERO para sair): ")
    if valor_str.isdigit() or valor_str.startswith('-'):
        #pass
        valor = int(valor_str)
        if valor == 0:
            break
        if valor > maior:
            maior = valor 
        if valor < menor:
            menor = valor
    else:
        print("Entrada inválida")
if maior == float("-inf"):
    print("Nenhum valor foi informado")
else:
    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")

#ou

valores = []
while True:
    valores_str = input("Informe um valor (0 para sair): ")
    if valores_str.isdigit() or valores_str.startswith("-"):
        if valores_str != "0":
            valores.append(int(valores_str))
        else:
            break
print(f"O valor máximo é: {max(valores)}")
print(f"O valor mínimo é: {min(valores)}")

#Questão 3
valores = []
while True:
    valores_str = input("Informe um valor (0 para sair): ")
    if valores_str.isdigit() or valores_str.startswith("-"):
        if valores_str != "0":
            valores.append(int(valores_str))
        else:
            break
print(f"O valor máximo é: {max(valores)}")
print(f"O valor mínimo é: {min(valores)}")

#Questão 4
valores = []
while True:
    valores_str = input("Informe um valor (0 para sair): ")
    if valores_str.isdigit() or valores_str.startswith("-"):
        if valores_str != "0":
            valores.append(int(valores_str))
        else:
            break
valores_impares = []
media = 0
for i in range(len(valores)):
    if valores[i]%2 != 0:
        valores_impares.append(valores[i])
for x in range(len(valores_impares)):
    media += valores_impares[x]
print(media/len(valores_impares))
