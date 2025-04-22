#Recuperação de POO
#Questão 1
while True:
    #nota = int(input("Informe uma nota entre 0 e 10"))
    nota_str = input("Informe uma nota entre 0 e 10")
    if nota_str.isdigit():
        nota = int(nota_str)
        if 0 <= nota <= 10:
            print(f"A nota {nota} válida")
        else:
            print(f"A nota {nota} é inválida")
    else:
        print("Valor inserido inválido")

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
