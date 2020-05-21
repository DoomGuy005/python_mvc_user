class Pessoa:
    
    dados = {
        'nome' : '', 
        'sobrenome' : '', 
        'idade' : ''
    }

    def __init__(self, nome, sobrenome, idade):
        global dados
        dados = {
            'nome' : nome,
            'sobrenome' : sobrenome, 
            'idade' : idade
        }

    def getNome(self):
        global dados
        return dados['nome']

    def getSobrenome(self):
        global dados
        return dados['sobrenome']

    def getIdade(self):
        global dados
        return dados['idade']

    def getDados(self):
        global dados
        return dados

    def setNome(self, x):
        global dados
        dados['nome'] = x

    def setSobrenome(self, x):
        global dados
        dados['sobrenome'] = x

    def setIdade(self, x):
        global dados
        dados['idade'] = x

    def removeNome(self):
        global dados
        dados['nome'] = ''
    
    def removeSobrenome(self):
        global dados
        dados['sobrenome'] = ''

    def removeIdade(self):
        global dados
        dados['idade'] = ''