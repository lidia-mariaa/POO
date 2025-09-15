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

1. Classe é como um molde ou plano, ela define oque todo objeto associado a ela deve ter;

2. Objeto é o produto real baseado nesse molde;

3. Self é um parâmetro que faz referência ao próprio objeto -> ele é usado dentro da classe para acessar os atributos e métodos do objeto atual. Self permite que a classe “saiba” a qual objeto específico ela está se referindo naquele momento.

'''

class Pessoa: #Você criou a classe Pessoa
    def __init__(self, nome, idade): # Nome e idade são parâmetros do método "__init__" -> vou explicar ele abaixo
        self.nome = nome # Atributo - características que o objeto vai guardar. -> aqui, o valor de nome que foi passado é guardado dentro do objeto
        self.idade = idade # Atributo - características que o objeto vai guardar.-> aqui, o valor de idade que foi passado é guardado dentro do objeto

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
'''
O __init__ é um contrutor, ou seja, ele é um método especial em uma classe que é executado automaticamente quando um objeto é criado.
'''
# Ex.:
class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Ana", 25) # chama o construtor __init__
# Dentro do __init__, o Python atribui: self.nome = "Ana" e self.idade = 25
# O objeto p1 agora tem essas características.
print(p1.nome)   # Ana
print(p1.idade)  # 25
# O construtor (__init__) é usado para criar e configurar um objeto assim que ele nasce.


# Ex. de classe com demais métodos para o objeto:

class Carro:
    def __init__(self, marca):
        self.marca = marca
        self.velocidade = 0 # Já velocidade não precisa ser informada pelo usuário ao criar o objeto, porque todo carro novo começa parado. A velocidade inicial é sempre zero, então faz sentido definir um valor fixo no código, e não pedir como entrada.
        # OBS.: Você só torna algo um parâmetro quando quer que o valor seja fornecido de fora (pelo usuário, por exemplo).

    def acelerar(self): # Método = comportamento (ação)
        self.velocidade += 10 # Atributo = característica (estado) -> o atributo, pode ou não vir como parâmetro, como vimos acima com o caso da velocidade.
        print(f"{self.marca} acelerou. Velocidade atual: {self.velocidade} km/h")

    def frear(self):
        if self.velocidade >= 10:
            self.velocidade -= 10
        else:
            self.velocidade = 0
        print(f"{self.marca} freou. Velocidade atual: {self.velocidade} km/h")

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota")

# Usando métodos
meu_carro.acelerar()  # Toyota acelerou. Velocidade atual: 10 km/h
meu_carro.acelerar()  # Toyota acelerou. Velocidade atual: 20 km/h
meu_carro.frear()     # Toyota freou. Velocidade atual: 10 km/h
