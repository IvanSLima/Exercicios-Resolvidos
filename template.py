from typing_extensions import Self


class Caneca:
    formato = 'Cilindrico com alça'

    def __init__(self, nome, logo, cor):
        self.nome = nome
        self.logo = logo
        self.cor = cor
        self.status = 'Cheia'

    def beber(self):
        self.status = 'Vazia'

    def encher(self):
        self.status = 'Cheia'


caneca1 = Caneca('Caneca Da uber', 'Logo Da Uber', 'Branca')
caneca2 = Caneca('Caneca Da Disney', 'Logo Da Disney', 'Branca')

print('A', caneca1.nome, 'Possui a ', caneca1.logo)
print('A', caneca2.nome, 'Possui a ', caneca2.logo)
