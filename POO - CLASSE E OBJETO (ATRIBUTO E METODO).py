#POO - CLASSE E OBJETO (ATRIBUTO E METODO)

'''
POO significa Programação Orientada a Objetos.

É um jeito de programar que organiza o código em "objetos", como se você estivesse modelando coisas do mundo real.

Em vez de ficar criando código solto, você cria um objeto que tem:

a) Atributos (Caraceterísticas, coisas que ele tem)
b) Métodos (coisas que ele faz)
Obs.: Para ser função precisa do 'return', o método também pode ter o 'return', porém, para ser método precisa do parâmetro 'self', ou seja:
parâmetro -> sem return
função -> com return
método -> com self

-----------------------------------------------------------------

1. Classe é como um molde ou plano;

2. Objeto é o produto real baseado nesse molde;

3. Self é um parâmetro que faz referência ao próprio objeto -> ele é usado dentro da classe para acessar os atributos e métodos do objeto atual. Self permite que a classe “saiba” a qual objeto específico ela está se referindo naquele momento.

'''

class Pessoa:
    def __init__(self, nome, idade): # Nome e idade são parâmetros do método "__init__" -> vou explicar ele abaixo
        self.nome = nome # Atributo - características que o objeto vai guardar.
        self.idade = idade # Atributo - características que o objeto vai guardar.

p1 = Pessoa("Maria", 30) # Você criou um objeto chamado p1, que é uma pessoa. Essa pessoa tem nome = "Maria" e idade = 30
# Ou seja, o valor do parâmetro nome ("Maria") é guardado no atributo self.nome do objeto p1

print(p1.nome)   # Resultado: Maria
print(p1.idade)  # Resultado: 30

'''
O "__init__" é um método especial dentro da classe em Python. Ele serve para "inicializar" um objeto quando você cria ele. É como a primeira coisa que acontece quando você cria um objeto novo.

-> Por que ele existe?

Quando você cria um objeto, você quer que ele já comece com algumas características (atributos) configuradas, certo?

O __init__ é o lugar onde você diz quais informações o objeto precisa ter logo que nascer. Sem ele, o objeto nasce "vazio"
'''
