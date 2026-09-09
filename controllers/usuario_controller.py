# Importa o APIRouter.
# Ele permite criar e organizar as rotas da API.
from fastapi import APIRouter

from models.usuario import usuario
from schema.usuario_schema import UsuarioSchema
from service.usuario_service import UsuarioService


router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)


service = UsuarioService()


# ============================================================
# CADASTRAR USUÁRIO
# ============================================================

# Define a rota POST para cadastrar um usuário.
@router.post("/")
def cadastrar(usuario_schema: UsuarioSchema):
    usuario_model = usuario(
        cpf=usuario_schema.cpf,
        sexo=usuario_schema.sexo,
        data_de_nascimento=usuario_schema.data_de_nascimento,
        nome=usuario_schema.nome,
        id_perfil=usuario_schema.id_perfil,
        email=usuario_schema.email,
        senha=usuario_schema.senha,
    )

    service.cadastrar(usuario_model)

    return {"mensagem": "Usuário cadastrado com sucesso."}