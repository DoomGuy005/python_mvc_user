from Pessoa import Pessoa as p
from ViewV import View as v
import os
from time import sleep

class Control:
    
    def __init__(self):
        self.model = p('','','')
        self.view = v()

    def start(self):
        os.system('cls')
        v.msgHome()
        sleep(2)
        os.system('cls')
        p.setNome(self,input(v.msgNome()))
        p.setSobrenome(self,input(v.msgSNome()))
        p.setIdade(self,input(v.msgIdade()))
        v.SucessCreate()
        sleep(2)
        os.system('cls')
        opcao = v.MenuMain()
        while opcao != 0:
            self.menuHandler(opcao)
    
    def menuHandler(self,opcao):
        if opcao == '1':
            op_alt = v.MenuAlter()
            if op_alt == '1':
                v.msgNome()
                p.setNome(self,input())
                v.SucessUpdateNome()
                sleep(2)
                os.system('cls')
                v.MenuAlter()
            elif op_alt == '2':
                v.msgSNome()
                p.setSobrenome(self,input())
                v.SucessUpdateSNome()
                sleep(2)
                os.system('cls')
                v.MenuAlter()
            elif op_alt == '3':
                v.msgIdade()
                p.setIdade(self,input())
                v.SucessUpdateIdade()
                sleep(2)
                os.system('cls')
                v.MenuAlter()
            elif op_alt == '4':
                os.system('cls')
                opcao = v.MenuMain()
                while opcao != 0:
                    self.menuHandler(opcao)
        elif opcao == '2': #Apagar Usuário
            p.removeNome(self)
            p.removeSobrenome(self)
            p.removeIdade(self)
            v.UserDeleted()
            sleep(2)
            os.system('cls')
            opcao = v.MenuMain()
            while opcao != 0:
                self.menuHandler(opcao)
        elif opcao == '3': #Checar Usuário
            v.ShowUser(p.getNome(self), p.getSobrenome(self), p.getIdade(self))
            sleep(2)
            os.system('cls')
            opcao = v.MenuMain()
            while opcao != 0:
                self.menuHandler(opcao)
        elif opcao == '4':
            v.Sair()
        else:
            print('>> Digitai uma opção correta, manéu!')
            sleep(2)
            os.system('cls')
            opcao = v.MenuMain()
            while opcao != 0:
                self.menuHandler(opcao)
if __name__ == "__main__":
    main = Control()
    main.start()