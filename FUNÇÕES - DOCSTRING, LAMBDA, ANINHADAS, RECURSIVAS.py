# FUNÇÕES - DOCSTRING, LAMBDA, ANINHADAS, RECURSIVAS

# a) Docstring 
# Docstring (document string) é uma string de documentação usada para descrever o propósito de uma função, classe ou módulo em Python. Ela aparece logo após a definição de uma função (ou classe/módulo) e é escrita entre aspas triplas (""" """ ou ''' ''').

def soma(a, b):
    """
    Soma dois números e retorna o resultado.

    Parâmetros:
    a (int ou float): O primeiro número.
    b (int ou float): O segundo número.

    Retorna:
    int ou float: A soma de a e b.
    """
    return a + b

# -> Como acessar a docstring?
# Você pode usar a função help() ou o atributo .__doc__:

help(soma)
#Ou:
print(soma.__doc__)

# b) Funções Aninhadas
# Funções aninhadas são funções definidas dentro de outras funções. Ou seja, você cria uma função interna dentro do corpo de outra função.

def calcular_total(preco):
    imposto = 0.1  # 10%

    def adicionar_imposto():
        return preco * imposto
    
    return preco + adicionar_imposto()

# A função interna pode acessar variáveis da função externa
# A função interna não é visível fora da função externa:

calcular_total(100)   # ok
#adicionar_imposto()   # erro: não existe fora da função!

# Por que usar?
# Organização: Quando uma lógica é usada apenas dentro de uma função, faz sentido "esconder" ela ali dentro.

# c) Função Recursiva
# Recursão é quando uma função chama a si mesma para resolver um problema. A ideia é dividir o problema em partes menores, até chegar a um caso tão simples que a função possa resolvê-lo diretamente (o chamado caso base).

# -> Estrutura de uma função recursiva:
# Caso base: quando parar a recursão.
# Chamada recursiva: quando a função se chama novamente com um problema menor.

#Ex.:
def contar_regressivo(n):
    if n == 0:           #Caso Base
        print("FIM!")
    else:
        print(n)
        contar_regressivo(n - 1)  #Chamada recursiva

'''
Resultado:
5
4
3
2
1
FIM!

Como funciona?
1- A função recebe o número n.
2- Se n ainda não é zero, ela:
imprime o número,
Chama a si mesma com n - 1 (um número menor).
3- Quando n chega em 0, ela imprime "FIM!" e para.
'''

'''
⚠️ Cuidado!
Se você não definir um caso base, a função nunca para e gera um erro de recursão (stack overflow):
'''
#Ex.:
def erro():
    return erro()

# d) Função Lambda
# Uma função lambda é uma função anônima, ou seja, sem nome, usada para códigos simples e rápidos. Ela é escrita em uma única linha e serve para fazer coisas pequenas, como uma operação matemática.

# -> Estrutura:
# lambda argumentos: expressão

# -> Características:
# Não precisa de def nem nome.
# Ideal para funções pequenas (como somar, dobrar, ordenar).
# Só pode conter 1 expressão (sem comandos como print, for, etc).

# Ex.:
# Soma dois números
soma = lambda a, b: a + b
print(soma(2, 3))  # saída: 5

# Dobro de um número
dobro = lambda x: x * 2
print(dobro(4))  # saída: 8

# Ordenar pelo tamanho do nome (número de letras)
nomes = ['João', 'Ana', 'Carlos']
ordenado = sorted(nomes, key = lambda nome: len(nome)) #essa parte define o critério de ordenação. O lambda cria uma função anônima que recebe um nome e retorna o seu comprimento (número de letras)
print(ordenado) #Então, o sorted() irá ordenar a lista com base no tamanho de cada nome.

# Resultado:
# ['Ana', 'João', 'Carlos']

'''
sorted -> Ordena uma lista, e você pode usar uma função lambda e um parâmetro key para dizer como ordenar. Ele necessita de um parâmetro, como a lista em que você vai aplicar o sorted, depois você põe e o key
key -> O parâmetro key serve para definir uma regra personalizada de ordenação.
➡️ Você passa uma função para key, e essa função vai dizer qual parte de cada item deve ser usada para comparar e ordenar.
Obs.: sorted(['banana', 'abacate', 'caju'])
# resultado: ['abacate', 'banana', 'caju']  (ordem alfabética)
'''
