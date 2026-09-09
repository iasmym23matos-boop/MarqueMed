from pydantic import BaseModel

class PerfilSchema(BaseModel):
    # Descrição do perfil.
    # Exemplos: 
    # paciente, 
    # medicos,
    #  clinicas, 
    # recepção
    ds_perfil: str
