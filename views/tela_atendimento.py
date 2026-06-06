class TelaAtendimento:
    def mostrar_mensagem(self, mensagem: str):
        print(f"\n[SISTEMA] {mensagem}")

    def mostrar_erro(self, mensagem: str):
        print(f"\n[ERRO] {mensagem}")

    def ler_dados_agendamento(self):
        print("\n--- Novo Agendamento ---")
        data_str = input("Data do atendimento (DD/MM/AAAA): ")
        horario_inicio = input("Horário de Início (HH:MM): ")
        horario_fim = input("Horário de Término (HH:MM): ")
        valor_base = float(input("Valor Base (R$): "))
        #IDs de paciente, clinica, etc. seriam lidos aqui e buscados no Controller
        return data_str, horario_inicio, horario_fim, valor_base

    def ler_dados_pagamento(self):
        print("\n--- Registro de Pagamento ---")
        modalidade = input("Modalidade (1-Dinheiro, 2-PIX, 3-Cartão): ")
        valor = float(input("Valor a pagar (R$): "))
        return modalidade, valor