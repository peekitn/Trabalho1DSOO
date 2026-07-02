from daos.dao import DAO
from models.atendimento import Atendimento

class AtendimentoDAO(DAO):
    def __init__(self):
        super().__init__('atendimentos.pkl')

    def add(self, atendimento: Atendimento):
        if (atendimento is not None) and isinstance(atendimento, Atendimento):
            # Gera uma chave única combinando CPF do paciente + Data + Hora
            # Ex: "12345678900_2026-07-02_08:00"
            chave = f"{atendimento.paciente.cpf}_{atendimento.data_atendimento}_{atendimento.horario_inicio}"
            super().add(chave, atendimento)

    def get(self, chave: str):
        if isinstance(chave, str):
            return super().get(chave)

    def remove(self, chave: str):
        if isinstance(chave, str):
            return super().remove(chave)