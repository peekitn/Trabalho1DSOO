from abc import ABC, abstractmethod
from datetime import date
from models.pessoas import Paciente

class Pagamento(ABC):
    def __init__(self, data: date, paciente: Paciente, valor_pago: float):
        self.data = data
        self.paciente = paciente
        self.valor_pago = valor_pago
        self.atendimento_vinculado = None

    @property
    def valor_pago(self):
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, valor):
        if valor <= 0:
            raise ValueError("O valor pago deve ser maior que zero.")
        self.__valor_pago = valor

    @abstractmethod
    def get_descricao(self):
        pass


class PagamentoDinheiro(Pagamento):
    def __init__(self, data: date, paciente: Paciente, valor_pago: float):
        super().__init__(data, paciente, valor_pago)
        
    def get_descricao(self):
        return "Pagamento em Dinheiro"


class PagamentoPix(Pagamento):
    def __init__(self, data: date, paciente: Paciente, valor_pago: float, cpf_pagador: str):
        super().__init__(data, paciente, valor_pago)
        self.cpf_pagador = cpf_pagador
        
    def get_descricao(self):
        return "Pagamento via PIX"


class PagamentoCartao(Pagamento):
    def __init__(self, data: date, paciente: Paciente, valor_pago: float, numero_cartao: str, bandeira: str):
        super().__init__(data, paciente, valor_pago)
        self.numero_cartao = numero_cartao
        self.bandeira = bandeira
        
    def get_descricao(self):
        return "Pagamento via Cartão"