# Importa o BaseModel do Pydantic.
# O FastAPI utiliza o Pydantic para validar
# os dados recebidos nas requisições.
from pydantic import BaseModel
from datetime import date
from typing import Optional


class UsuarioSchema(BaseModel):
    cpf: str
    sexo: Optional[str] = None
    data_de_nascimento: Optional[date] = None
    nome: str
    id_perfil: Optional[int] = None
    email: str
    senha: str