import requests


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def obter_todos_os_dados(self):
        resposta = requests.get(
            'https://www.youtube.com/watch?v=ISNT3lkY6NA&ab_channel=DeSola')

        if resposta.ok:
            return 'CONECTADO COM SUCESSO'
        else:
            return 'ERRO 404'
