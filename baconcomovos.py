'''
1 - receber um numero inteiro
2 - saber se o numero é multiplo de 3 e 5 
    Bacon com ovos
3 - Saber se o numero é multiplo somente de 3:
    Bacon
4 - Saber se o numero é multiplo somente de 5:
    Ovos
5 - Saber se o numero NÃO é multiplo de 3 nem de 5:
    Passa fome
'''


def bacon_com_ovos(n):
    assert isinstance(n, int), '"n" deve ser inteiro'

    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com ovos'

    if n % 3 == 0:
        return 'Bacon'

    if n % 5 == 0:
        return 'Ovos'

    return 'Passar fome'
