# - Lídia Maria L. Lopes

# Problema 1 - Publicações

# Classe base -> Publicacao
class Publicacao:
    def __init__(self, titulo, ano_publicacao):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao

    def descrever(self): # Possui o método descrever que imprime o título e o ano de publicação.
        print(f"Título: {self.titulo}")
        print(f"Ano de publicação: {self.ano_publicacao}")

# Classe Livro -> herda de Publicacao
class Livro(Publicacao):
    def __init__(self, titulo, ano_publicacao, autor): # Adicionei o método autor
        super().__init__(titulo, ano_publicacao) # Referenciando a classe pai usando o super()
        self.autor = autor

    def descrever(self):
        super().descrever()  # Chamando o método descrever da classe base
        print(f"Autor: {self.autor}")

# Classe Revista -> herda de Publicacao
class Revista(Publicacao):
    def __init__(self, titulo, ano_publicacao, edicao):
        super().__init__(titulo, ano_publicacao) # Referenciando a classe pai usando o super()
        self.edicao = edicao

#---

# Problema 3 - Sistema de Funcionários

# Classe base -> Funcionario
class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):

        return self.salario_base # Retorna o salário base por padrão

# Classe Gerente -> herda de Funcionario
class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base) # Referenciando a classe base (Funcionario)
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario_base + self.bonus # Retorna o salário base mais o bônus

# Classe Programador -> herda de Funcionario
class Programador(Funcionario):
    def __init__(self, nome, salario_base, horas_extras, valor_hora_extra):
        super().__init__(nome, salario_base) # Referenciando a classe base (Funcionario)
        self.horas_extras = horas_extras
        self.valor_hora_extra = valor_hora_extra

    def calcular_salario(self):
        return self.salario_base + (self.horas_extras * self.valor_hora_extra) # Retorna o salário base mais o total das horas extras

# Teste do sistema de funcionários
if __name__ == "__main__":
    # Criando uma lista heterogênea de funcionários
    funcionarios = [
        Gerente("Lídia", 5000, 1000),  # Gerente com bônus
        Programador("Nicoly", 4000, 10, 50),  # Programador com horas extras
        Gerente("Isabelly", 6000, 1500),  # Outro Gerente com bônus
        Programador("Débora", 3500, 5, 60)  # Outro Programador com horas extras
    ]

    # Iterando sobre a lista de funcionários e exibindo o nome e o salário calculado
    for funcionario in funcionarios:
        print(f"{funcionario.nome}: R${funcionario.calcular_salario():.2f}")
    def descrever(self):
        super().descrever()  # Chamando o método descrever da classe base
        print(f"Edição: {self.edicao}")
        
#---

# Problema 2 - Veículos e Seus Atributos

# Classe base -> Veiculo
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")

# Classe Carro -> herda de veículo
class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas): # Adicionei o atributo numero_portas
        super().__init__(marca, modelo) # Referenciando a classe pai (Veiculo)
        self.numero_portas = numero_portas

    def exibir_info(self): # Chamando o método exibir_info da classe pai e exibindo os atributos do carro
        super().exibir_info()
        print(f"Número de portas: {self.numero_portas}")

# Classe Moto -> herda de veículo
class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo) # Referenciando a classe pai (Veiculo)
        self.cilindradas = cilindradas

    def exibir_info(self):
        super().exibir_info() # Chamando o método exibir_info da classe pai e exibindo os atributos da moto
        print(f"Cilindradas: {self.cilindradas}")
