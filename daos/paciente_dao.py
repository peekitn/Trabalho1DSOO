from daos.dao import DAO
from models.pessoas import Paciente

class PacienteDAO(DAO):
    def __init__(self):
        super().__init__('pacientes.pkl')

    def add(self, paciente: Paciente):
        # aqui verifica se o CPF é string e se o objeto é da classe Paciente
        if (isinstance(paciente.cpf, str)) and (paciente is not None) and isinstance(paciente, Paciente):
            super().add(paciente.cpf, paciente)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)