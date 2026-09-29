# Importa a classe Usuario.
# Essa classe representa o modelo dos dados do usuário.
from models.usuario import Usuario

# Importa o Repository responsável pelo acesso
# aos dados da tabela usuario no banco SQLite.
from repositories.usuario_repository import UsuarioRepository

# Cria a classe responsável pelas regras de negócio
# relacionadas aos usuários.
class UsuarioService:

    # Método construtor da classe.
    def __init__(self):

        # Cria uma instância do UsuarioRepository.
        #
        # O Service utilizará o Repository sempre que
        # precisar consultar ou alterar o banco de dados.
        self.repository = UsuarioRepository()

    # ============================================================
    # CADASTRAR USUÁRIO
    # ============================================================

    # Método responsável por cadastrar um novo usuário.
    def cadastrar(self, usuario: Usuario):

        # Verifica se o nome foi informado.
        if not usuario.nome:
            raise ValueError("O nome do usuário é obrigatório.")

        # Verifica se o CPF foi informado.
        if not usuario.cpf:
            raise ValueError("O CPF do usuário é obrigatório.")

        # Verifica se o CEP foi informado.
        if not usuario.cep:
            raise ValueError("O CEP do usuário é obrigatório.")

        # Verifica se o e-mail foi informado.
        if not usuario.email:
            raise ValueError("O e-mail do usuário é obrigatório.")

        # Verifica se a senha foi informada.
        if not usuario.senha:
            raise ValueError("A senha do usuário é obrigatória.")

        # Verifica se o perfil foi informado.
        if not usuario.id_perfil:
            raise ValueError("O perfil do usuário é obrigatório.")

        # Verifica se a data de nascimento foi informada.
        if not usuario.data_de_nascimento:
            raise ValueError("A data de nascimento é obrigatória.")

        # Verifica se o sexo foi informado.
        if not usuario.sexo:
            raise ValueError("O sexo é obrigatório.")

        # Consulta o banco para verificar se já existe
        # um usuário utilizando o mesmo e-mail.
        usuario_existente = self.repository.buscar_por_email(
            usuario.email
        )

        # Verifica se foi encontrado algum usuário.
        if usuario_existente:
            raise ValueError(
                "Já existe um usuário cadastrado com este e-mail."
            )

        # Depois que todas as regras foram validadas,
        # envia o usuário para o Repository realizar
        # a gravação no banco e retorna o id criado.
        return self.repository.inserir(usuario)

    # ============================================================
    # LISTAR USUÁRIOS
    # ============================================================
    def listar(self):
        return self.repository.listar()

    # ============================================================
    # BUSCAR USUÁRIO POR ID
    # ============================================================
    def buscar_por_id(self, id_usuario):

        if not id_usuario:
            raise ValueError("O ID do usuário é obrigatório.")

        usuario = self.repository.buscar_por_id(id_usuario)

        if not usuario:
            raise ValueError("Usuário não encontrado.")

        return usuario

    # ============================================================
    # ATUALIZAR USUÁRIO
    # ============================================================
    def atualizar(self, usuario: Usuario):

        if not usuario.id_usuario:
            raise ValueError("O ID do usuário é obrigatório.")

        usuario_existente = self.repository.buscar_por_id(
            usuario.id_usuario
        )

        if not usuario_existente:
            raise ValueError("Usuário não encontrado.")

        if not usuario.nome:
            raise ValueError("O nome do usuário é obrigatório.")

        if not usuario.cpf:
            raise ValueError("O CPF do usuário é obrigatório.")

        if not usuario.cep:
            raise ValueError("O CEP do usuário é obrigatório.")

        if not usuario.email:
            raise ValueError("O e-mail do usuário é obrigatório.")

        if not usuario.id_perfil:
            raise ValueError("O perfil do usuário é obrigatório.")

        if not usuario.data_de_nascimento:
            raise ValueError("A data de nascimento é obrigatória.")

        if not usuario.sexo:
            raise ValueError("O sexo é obrigatório.")

        usuario_email = self.repository.buscar_por_email(usuario.email)

        if usuario_email:
            uid = usuario_email.get('id_usuario') if isinstance(usuario_email, dict) else getattr(usuario_email, 'id_usuario', None)
            if uid != usuario.id_usuario:
                raise ValueError("O e-mail informado já está sendo utilizado.")

        self.repository.atualizar(usuario)

    # ============================================================
    # EXCLUIR USUÁRIO
    # ============================================================
    def excluir(self, id_usuario):

        if not id_usuario:
            raise ValueError("O ID do usuário é obrigatório.")

        usuario = self.repository.buscar_por_id(id_usuario)

        if not usuario:
            raise ValueError("Usuário não encontrado.")

        self.repository.excluir(id_usuario)

    # ============================================================
    # LOGIN
    # ============================================================
    def login(self, email, senha):

        if not email:
            raise ValueError("O e-mail é obrigatório.")

        if not senha:
            raise ValueError("A senha é obrigatória.")

        # Suporte temporário para usuário administrador local
        if email == 'admin' and senha == '1234':
            return {
                'id_usuario': 0,
                'cpf': '',
                'cep': '',
                'nome': 'Administrador',
                'id_perfil': 0,
                'email': 'admin',
                'senha': senha,
                'data_nascimento': '',
                'sexo': '',
                'ds_perfil': 'Administrador'
            }

        usuario = self.repository.buscar_por_email(email)

        if not usuario:
            raise ValueError("E-mail ou senha inválidos.")

        senha_armazenada = usuario.get('senha') if isinstance(usuario, dict) else getattr(usuario, 'senha', None)

        if senha_armazenada != senha:
            raise ValueError("E-mail ou senha inválidos.")

        return usuario