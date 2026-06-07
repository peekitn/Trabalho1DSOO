from datetime import date
from models.pessoas import Paciente, Profissional
from models.pagamentos import Pagamento

class MenorDeIdadeException(Exception):
    def __init__(self, mensagem="Paciente menor de idade não pode agendar sozinho."):
        super().__init__(mensagem)

class ForaDoHorarioComercialException(Exception):
    def __init__(self, mensagem="Horário fora do expediente da clínica (08:00 às 18:00)."):
        super().__init__(mensagem)

class PagamentoAtrasadoException(Exception):
    def __init__(self, mensagem="O pagamento está atrasado."):
        super().__init__(mensagem)

class ValorInvalidoException(Exception):
    def __init__(self, mensagem="O valor inserido para pagamento é inválido."):
        super().__init__(mensagem)

class Clinica:
    def __init__(self, nome: str, cidade: str, descricao: str):
        self.nome = nome
        self.cidade = cidade
        self.descricao = descricao


class TipoAtendimento:
    def __init__(self, nome: str):
        self.nome = nome  # ex: "Consulta", "Exame", "Retorno"


class Procedimento:
    def __init__(self, descricao: str, custo: float, profissional: Profissional):
        self.descricao = descricao
        self.custo = custo
        self.profissional = profissional


class Atendimento:
    def __init__(self, clinica: Clinica, paciente: Paciente, profissional: Profissional, 
                 data_atendimento: date, horario_inicio: str, horario_fim: str, 
                 tipo: TipoAtendimento, valor_base: float):
        
        # aqui entra a validação de Regra de Negócio (exemplo para o controlador usar depois)
        if not paciente.is_maior_de_idade():
            raise ValueError("Pacientes menores de 18 anos não podem realizar atendimento independente.")
            
        self.clinica = clinica
        self.paciente = paciente
        self.profissional = profissional
        self.data_atendimento = data_atendimento
        self.horario_inicio = horario_inicio
        self.horario_fim = horario_fim
        self.tipo = tipo
        self.valor_base = valor_base
        
        # Composição
        self.__procedimentos = []
        self.__pagamentos = []

    def adicionar_procedimento(self, procedimento: Procedimento):
        self.__procedimentos.append(procedimento)

    def registrar_pagamento(self, pagamento: Pagamento):
        pagamento.atendimento_vinculado = self
        self.__pagamentos.append(pagamento)

    def calcular_valor_total(self) -> float:
        total_procedimentos = sum(p.custo for p in self.__procedimentos)
        return self.valor_base + total_procedimentos

    def calcular_valor_restante(self) -> float:
        total_pago = sum(p.valor_pago for p in self.__pagamentos)
        return self.calcular_valor_total() - total_pago