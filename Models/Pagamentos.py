from abc import ABC, abstractmethod # Permite a criacão de classes abstratas e métodos abstratos
from datetime import date # Ajuda para trabalhar com datas reais
from pessoas import Paciente # Para que o pagamento saiba exatamente quem é a pessoa que está pagando, criando uma associação direta entre os objetos

class Pagamento(ABC):
    def __init__(self, data: date, paciente: Paciente, valor_pago: float):
        self.data = data
        self.paciente = paciente
        self.valor_pago = valor_pago
        self.atendimento_vinculado = None  # No momento em que o Pagamento é criado, ele nasce com a data, o paciente e o valor, mas ele ainda não sabe a qual consulta ou exame (atendimento) ele pertence.

    @property
    def valor_pago(self):
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, valor):
        if valor <= 0:
            raise ValueError("O valor pago deve ser maior que zero.") # Tratamento de erro caso o valor inserido for menor que 0
        self.__valor_pago = valor


class PagamentoDinheiro(Pagamento):
    def __init__(self, data: date, paciente: Paciente, valor_pago: float):
        super().__init__(data, paciente, valor_pago)


class PagamentoPix(Pagamento):
    def __init__(self, data: date, paciente: Paciente, valor_pago: float, cpf_pagador: str):
        super().__init__(data, paciente, valor_pago)
        self.cpf_pagador = cpf_pagador


class PagamentoCartao(Pagamento):
    def __init__(self, data: date, paciente: Paciente, valor_pago: float, numero_cartao: str, bandeira: str):
        super().__init__(data, paciente, valor_pago)
        self.numero_cartao = numero_cartao
        self.bandeira = bandeira