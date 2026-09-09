from datetime import date


class usuario:
    def __init__(self,
                 id_usuario=0,
                 cpf="",
                 cep="",
                 nome="",
                 id_perfil=0,
                 email="",
                 senha="",
                 data_de_nascimento=None,
                 sexo=None,
                 tipo=None):

        self.id_usuario = id_usuario
        self.cpf = cpf
        self.cep = cep
        self.nome = nome
        self.id_perfil = id_perfil
        self.email = email
        self.senha = senha
        self.sexo = sexo
        self.tipo = tipo

        if data_de_nascimento is None:
            self.data_de_nascimento = date.today()
        else:
            self.data_de_nascimento = data_de_nascimento
