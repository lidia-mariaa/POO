#EXERCÍCIO PRESENTE NO SLIDE DE TUPLAS

#1 – Gere tupla dinamicamente de tamanho 5, de valores aleatório entre 1 e 20
from random import randint
numeros = []
for i in range(5):
    numeros.append(randint(1, 20))
print(tuple(numeros))

#2 – Verifique se um determinado elemento esta contido na tupla ('a','b',1,2,'c',3,4,'d',5)

tupla = ('a','b',1,2,'c',3,4,'d',5)
elemento = input("Informe um elemento: ")
tipo = input("informe o tipo do elemento: ")
if tipo == "int":
    if int(elemento) in tupla:
        print("está")
    else:
        print("não está")
if tipo == "float":
    if float(elemento) in tupla:
        print("está")
    else:
        print("não está")
if tipo == "bool":
    if bool(elemento) in tupla:
        print("está")
    else:
        print("não está")
if tipo == "str":
    if str(elemento) in tupla:
        print("está")
    else:
        print("não está")

#3 – Dada uma tupla de nomes de alunos e suas respectivas notas, escreva um programa que imprima o nome do aluno com a maior nota e o nome do aluno com a menor nota.
#alunos = (("João", 8.5), ("Maria", 9.2), ("José", 7.1), ("Ana", 8.7), ("Carlos", 6.5))

alunos = (("João", 8.5), ("Maria", 9.2), ("José", 7.1), ("Ana", 8.7), ("Carlos", 6.5))
notas = []
for i in range(len(alunos)):
    notas.append(alunos[i][-1])
print(f"A maior nota foi {max(notas)}")
print(f"A menor nota foi {min(notas)}")

