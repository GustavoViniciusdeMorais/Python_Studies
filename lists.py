# -*- coding: utf-8 -*-

class List(object):
    
    def __init__(self, list):
        self.list = list
    
    def add(self, item):
        self.list.append(item)

    def describe(self):
        for v in self.list:
            print("{}".format(v))
    
    def remove(self, id):
        del self.list [id]

class App(object):

    def __init__(self):
        self.list = List(['a', 'b'])
    
    def choose(self):
        print('Escolha uma ação da lista')
        print('1- Adicionar item')
        print('2- Listar items')
        print('3- Remover item')
        action = raw_input('Digite o número da opção:')

        switcher = {
            1: self.add()
        }
    
    def add(self):
        item = raw_input('Digite o nome do item:')
        self.list.add(item)
        self.list.describe()

app = App()
app.choose()