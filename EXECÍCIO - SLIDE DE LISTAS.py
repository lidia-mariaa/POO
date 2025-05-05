#EXERCÍCIO PROPOSTO NO SLIDE DE LISTAS

#1) Ler uma lista de 5 número inteiros e imprimir
# cada número juntamente com a sua posição na lista.

lista_1 = ["a", "b", "c", "d", "e"]
for i in range(len(lista_1)):
    print(f"Valor {lista_1[i]} na posição {i}")

#2) Ler uma lista de 5 número reais e imprimir a lista na ordem inversa.

lista_2_1 = ["1", "2", "3", "4", "5"]
lista_2_1.reverse() #por ser uma função não podemos por no print direto
print(lista_2_1)

#também pode ser:

lista_2_2 = ["1", "2", "3", "4", "5"]
lista_2_2_modificada = []
for i in range(len(lista_2_2)):
    lista_2_2_modificada.append(lista_2_2[-(i+1)])
print(lista_2_2_modificada)

#3) Ler uma lista de 4 notas e em seguida mostra as notas e a média.

lista_3 = [10, 8, 9, 5]
media = 0
for i in range(len(lista_3)):
    print(lista_3[i])
    media += lista_3[i]
print(media/len(lista_3))

#4) Ler uma lista de 5 números e imprimir o menor e maior valor.

lista_4 = [1, 2, 3, 4, 5]
print(f"Maior valor: {max(lista_4)}")
print(f"Menor valor: {min(lista_4)}")
