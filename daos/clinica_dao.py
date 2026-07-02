from daos.dao import DAO
from models.atendimento import Clinica

class ClinicaDAO(DAO):
    def __init__(self):
        super().__init__('clinicas.pkl')

    def add(self, clinica: Clinica):
        if (clinica is not None) and isinstance(clinica, Clinica):
            # Cria a chave composta em minúsculas para padronizar
            chave = f"{clinica.nome.lower()}_{clinica.cidade.lower()}"
            super().add(chave, clinica)

    def get(self, chave: str):
        if isinstance(chave, str):
            return super().get(chave)

    def remove(self, chave: str):
        if isinstance(chave, str):
            return super().remove(chave)