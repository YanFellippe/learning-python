class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == 'mago':
            ataque = 'usou magia'
        elif self.tipo == 'guerreiro':
            ataque = 'usou espada'
        elif self.tipo == 'monge':
            ataque = 'usou artes marciais'
        elif self.tipo == 'ninja':
            ataque = 'usou shuriken'
        else:
            ataque = 'usou um ataque indefinido'

        print(f'O {self.tipo} atacou usando {ataque}')

heroi1 = Heroi('Aragorn', 30, 'guerreiro')
heroi2 = Heroi('Gandalf', 200, 'mago')
heroi3 = Heroi('Atunm', 80, 'monge')
heroi4 = Heroi('Jinka', 19, 'ninja')

heroi1.atacar()
heroi2.atacar()
heroi3.atacar()
heroi4.atacar()