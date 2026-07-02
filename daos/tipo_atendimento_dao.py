from daos.dao import DAO
from models.atendimento import TipoAtendimento

class TipoAtendimentoDAO(DAO):
    def __init__(self):
        super().__init__('tipos_atendimento.pkl')

    def add(self, tipo: TipoAtendimento):
        # Valida se é um objeto do tipo correto e usa o nome como chave
        if (tipo is not None) and isinstance(tipo, TipoAtendimento) and isinstance(tipo.nome, str):
            # Salva a chave sempre em minúsculas para evitar duplicação entre "Consulta" e "consulta"
            super().add(tipo.nome.lower(), tipo)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key.lower())

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key.lower())