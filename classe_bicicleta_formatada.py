class Bicicleta:
    # O método __init__ é o construtor da classe, chamado quando uma nova instância da classe é criada.
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor  # Define um atributo de instância chamado 'cor' e o inicializa com o valor fornecido.
        self.modelo = modelo  # Define um atributo de instância chamado 'modelo' e o inicializa com o valor fornecido.
        self.ano = ano  # Define um atributo de instância chamado 'ano' e o inicializa com o valor fornecido.
        self.valor = valor  # Define um atributo de instância chamado 'valor' e o inicializa com o valor fornecido.

    # O método __str__ define a representação em string da instância da classe.
    def __str__(self):
        # Retorna uma string formatada com o nome da classe e os atributos de instância.
        # As chaves (nomes dos atributos) são convertidas para que a primeira letra fique maiúscula.
        return f"{self.__class__.__name__}: {', '.join([f'{chave.capitalize()}={valor}' for chave, valor in self.__dict__.items()])}"

# Cria uma instância da classe Bicicleta com os valores fornecidos.
b2 = Bicicleta("Verde", "Monaco",2000 ,700)

