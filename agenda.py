def menu(*args):
    print('-' * 30)
    print('AGENDA'.center(30))
    print('-' * 30)
    for pos, i in enumerate(args):
        print(f'{pos+1} - {i}')
    print('-' * 30)


def entrada(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            return int(num)
        else:
            print('Insira uma opção válida')


class Pessoa:
    def __init__(self, name, age, height):
        self.__nome = name
        self.__idade = age
        self.__altura = height


class Agenda:
    def __init__(self):
        self.__pessoas = list()

    def armazena_pessoa(self, n, i, a):
        self.__pessoas.append(Pessoa(n, i, a))
        print(f'\033[1;31m{n.upper()} armazenado com sucesso!\033[m')

    def remove_pessoa(self, n):
        for pessoa in self.__pessoas:
            if pessoa.__dict__['_Pessoa__nome'] == n:
                self.__pessoas.remove(pessoa)
                return print(f'\033[1;31m{n.upper()} removido com sucesso!\033[m')
        print(f'\033[1;31m{n.upper()} não foi encontrado.\033[m')

    def busca_pessoa(self, n):
        for pos, pessoa in enumerate(self.__pessoas):
            if pessoa.__dict__['_Pessoa__nome'] == n:
                return print(f'\033[1;31m{n.upper()} está na {pos+1}ª posição.\033[m')
        print(f'\033[1;31m{n.upper()} não foi encontrado.\033[m')

    def imprime_agenda(self):
        for i in self.__pessoas:
            print(i.__dict__)

    def imprime_pessoa(self, indice):
        if indice <= len(self.__pessoas):
            return print(self.__pessoas[indice-1].__dict__)
        print(f'\033[1;31mNão há índice {indice} na agenda\033[m')


minha_agenda = Agenda()
while True:
    menu('Armazenar pessoa', 'Remover pessoa', 'Buscar pessoa', 'Imprimir agenda', 'Imprimir pessoa', 'Sair')
    op = entrada('Digite uma opção: ')
    if op == 1:
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        altura = float(input('Altura: '))
        minha_agenda.armazena_pessoa(nome, idade, altura)
    elif op == 2:
        nome = input('Nome: ')
        minha_agenda.remove_pessoa(nome)
    elif op == 3:
        nome = input('Nome: ')
        minha_agenda.busca_pessoa(nome)
    elif op == 4:
        minha_agenda.imprime_agenda()
    elif op == 5:
        index = int(input('Posição: '))
        minha_agenda.imprime_pessoa(index)
    elif op == 6:
        break
