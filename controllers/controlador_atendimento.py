from views.tela_atendimento import TelaAtendimento
from datetime import datetime, date
from models.atendimento import Atendimento, MenorDeIdadeException, ForaDoHorarioComercialException, PagamentoAtrasadoException, ValorInvalidoException
from models.pagamentos import PagamentoDinheiro, PagamentoPix, PagamentoCartao

class ControladorAtendimento:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__view = TelaAtendimento() 

    def _validar_idade_paciente(self, paciente, data_atendimento):
        data_nasc = paciente.data_nascimento
        idade = data_atendimento.year - data_nasc.year - ((data_atendimento.month, data_atendimento.day) < (data_nasc.month, data_nasc.day))
        
        if idade < 18:
            raise MenorDeIdadeException()

    def _validar_horario_clinica(self, horario_inicio: str):
        hora = int(horario_inicio.split(":")[0])
        if hora < 8 or hora >= 18:
            raise ForaDoHorarioComercialException()

    def agendar_atendimento(self, clinica, paciente, profissional, tipo_atendimento):
        try:
            data_str, h_inicio, h_fim, valor_base = self.__view.ler_dados_agendamento()
            data_atendimento = datetime.strptime(data_str, "%d/%m/%Y").date()

            self._validar_idade_paciente(paciente, data_atendimento)
            self._validar_horario_clinica(h_inicio)

            novo_atendimento = Atendimento(
                data_atendimento=data_atendimento,
                horario_inicio=h_inicio,
                horario_fim=h_fim,
                valor_base=valor_base,
                clinica=clinica,
                paciente=paciente,
                profissional=profissional,
                tipo=tipo_atendimento
            )

            self.__controlador_principal.atendimentos.append(novo_atendimento)
            self.__view.mostrar_mensagem("Atendimento agendado com sucesso!")
            return novo_atendimento

        except ValueError:
            self.__view.mostrar_erro("Formato de data ou numero invalido inserido.")
        except (MenorDeIdadeException, ForaDoHorarioComercialException) as e:
            self.__view.mostrar_erro(str(e))
        except Exception as e:
            self.__view.mostrar_erro(f"Erro inesperado: {str(e)}")

    def processar_pagamento(self, atendimento):
        try:
            self.__view.mostrar_mensagem(f"Valor restante: R$ {atendimento.calcular_valor_restante():.2f}")
            modalidade, valor = self.__view.ler_dados_pagamento()
            
            data_hoje = date.today()
            novo_pagamento = None

            if modalidade == '1':
                novo_pagamento = PagamentoDinheiro(data_hoje, valor, atendimento.paciente, atendimento)
            elif modalidade == '2':
                cpf = self.__view.ler_dados_pix() 
                novo_pagamento = PagamentoPix(data_hoje, valor, atendimento.paciente, atendimento, cpf)
            elif modalidade == '3':
                cartao, bandeira = self.__view.ler_dados_cartao() 
                novo_pagamento = PagamentoCartao(data_hoje, valor, atendimento.paciente, atendimento, cartao, bandeira)
            else:
                self.__view.mostrar_erro("Modalidade invalida.")
                return

            atendimento.registrar_pagamento(novo_pagamento)
            self.__view.mostrar_mensagem(f"Pagamento de R$ {valor:.2f} registrado. Restante: R$ {atendimento.calcular_valor_restante():.2f}")

        except (PagamentoAtrasadoException, ValorInvalidoException) as e:
            self.__view.mostrar_erro(str(e))

    def abrir_tela(self):
        while True:
            opcao = self.__view.tela_opcoes()
            
            if opcao == 1:
                self.__view.mostrar_mensagem("Funcao de agendar acionada!")
                # ARRUMAR DEPOIS
                # ARRUMAR DEPOIS
            elif opcao == 2:
                self.__view.mostrar_mensagem("Funcao de pagamento acionada!")
                # ARRUMAR DEPOIS
                # ARRUMAR DEPOIS
            elif opcao == 0:
                break
            else:
                self.__view.mostrar_erro("Opcao invalida.")