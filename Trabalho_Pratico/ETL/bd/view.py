from datetime import datetime
from decimal import *

class View():
    def inicio(self):
        return self.menu()

    def menu():
        print("MENU")
        print("1. Dataload de Pokemons")
        print("2. Remover Range Pokemons")
        print("3. Dataload de Região")
        print("4. Remover Regiões")
        print("5. Sair")
        
        option = int(input("Digite o numero da opcao desejada: "))

        return option

    def printStatus(self, status):
        if (status == 'sucesso'):
            print("Comando executado no banco de dados com sucesso")
        else:
            print(status)