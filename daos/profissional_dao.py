from daos.dao import DAO
from models.pessoas import Profissional

class ProfissionalDAO(DAO):
    def __init__(self):
        super().__init__('profissionais.pkl')

    def add(self, profissional: Profissional):
        # Verifica se o CPF é string e se o objeto é da classe Profissional
        if (isinstance(profissional.cpf, str)) and (profissional is not None) and isinstance(profissional, Profissional):
            super().add(profissional.cpf, profissional)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)