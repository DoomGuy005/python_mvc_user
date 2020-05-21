class View:
    
    @staticmethod
    def msgHome():
        return('>>> BEM VINDO AO USER CREATION SIMULATOR! <<<')
    
    @staticmethod
    def msgNome():
        return('>> Digite o nome do usuário: ')
    
    @staticmethod
    def msgSNome():
        return('>> Digite o sobrenome do usuário: ')
    
    @staticmethod
    def msgIdade():
        return('>> Digite a idade do usuário: ')

    @staticmethod
    def ShowNome(n):
        return('>> Nome do usuário: ' + n)

    @staticmethod
    def ShowSobrenome(n):
        return('>> Sobrenome do usuário: '+ n)

    @staticmethod
    def ShowIdade(n):
        return('>> Idade da pessoa: ' + n)

    @staticmethod
    def SucessUpdateNome():
        return('>> 1º nome alterado com sucesso! <<')
    
    @staticmethod
    def SucessUpdateSNome():
        return('>> 2º nome alterado com sucesso! <<')

    @staticmethod
    def SucessUpdateIdade():
        return('>> Idade alterada com sucesso! <<')
    
    @staticmethod
    def SucessSetName(n):
        return('>> Nome do usuário agora é:'+n+'!')
    
    @staticmethod
    def SucessSetSName(n):
        return('>> Sobrenome do usuário agora é:'+n+'!')
    
    @staticmethod
    def SucessSetIdade(n):
        return ('>> Idade do usuário agora é:' + n + '!')
    
    @staticmethod
    def SucessCreate():
        return ('>> Usuário Criado com sucesso!')
        
    @staticmethod
    def MenuMain():
        print('>> Selecionai a operação desejada:')
        print('>> 1 - Alterar Usuário;')
        print('>> 2 - Apagar Usuário;')
        print('>> 3 - Checar Usuário;')
        print('>> 4 - Sair do programa;')
        return (input('>> '))
    
    @staticmethod
    def ShowUser(n, sn, i):
        View.ShowNome(n)
        View.ShowSobrenome(sn)
        View.ShowIdade(i)

    @staticmethod
    def MenuAlter():
        print('>> ALTERAR USUÁRIO:')
        print('>> Selecionai a operação desejada:')
        print('>> 1 - Alterar nome;')
        print('>> 2 - Alterar sobrenome;')
        print('>> 3 - Alterar idade;')
        print('>> 4 - Voltar para menu principal;')
        return(input('>> '))

    @staticmethod
    def UserDeleted():
        print('Usuário deletado com sucesso!')

    @staticmethod
    def Sair():
        raise SystemExit
