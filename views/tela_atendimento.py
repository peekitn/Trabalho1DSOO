class TelaAtendimento:
    def mostrar_mensagem(self, mensagem: str):
        print(f"\n[SISTEMA] {mensagem}")

    def mostrar_erro(self, mensagem: str):
        print(f"\n[ERRO] {mensagem}")

    def tela_opcoes(self):
        print("\n--- Modulo de Atendimentos ---")
        print("1 - Agendar atendimento")
        print("2 - Listar atendimentos")
        print("3 - Alterar atendimento")
        print("4 - Excluir atendimento")
        print("5 - Registrar procedimento")
        print("6 - Listar procedimentos")
        print("7 - Alterar procedimento")
        print("8 - Remover procedimento")
        print("9 - Processar pagamento")
        print("10 - Listar pagamentos")
        print("11 - Alterar pagamento")
        print("12 - Remover pagamento")
        print("0 - Voltar")
        return int(input("Escolha a opcao: "))

    def ler_dados_agendamento(self):
        print("\n--- Dados do Agendamento ---")
        data_str = input("Data do atendimento (DD/MM/AAAA): ")
        horario_inicio = input("Horario de Inicio (HH:MM): ")
        horario_fim = input("Horario de Termino (HH:MM): ")
        valor_base = float(input("Valor Base (R$): "))
        return data_str, horario_inicio, horario_fim, valor_base

    def ler_dados_pagamento(self):
        print("\n--- Registro de Pagamento ---")
        modalidade = input("Modalidade (1-Dinheiro, 2-PIX, 3-Cartao): ")
        valor = float(input("Valor a pagar (R$): "))
        return modalidade, valor

    def ler_dados_pix(self):
        return input("Digite o CPF do pagador (PIX): ")

    def ler_dados_cartao(self):
        cartao = input("Numero do cartao: ")
        bandeira = input("Bandeira: ")
        return cartao, bandeira

    def pedir_cpf_paciente(self):
        return input("Digite o CPF do Paciente: ").strip()

    def pedir_cpf_profissional(self):
        return input("Digite o CPF do Profissional: ").strip()

    def pedir_nome_clinica(self):
        return input("Digite o Nome da Clinica: ").strip()

    def pedir_tipo_atendimento(self):
        return input("Tipo de Atendimento (Ex: Consulta, Exame): ").strip()

    def pedir_indice(self, mensagem):
        return int(input(mensagem))

    def ler_dados_procedimento(self):
        print("\n--- Registro de Procedimento ---")
        descricao = input("Descricao do procedimento: ").strip()
        custo = float(input("Custo do procedimento (R$): "))
        return descricao, custo

    def pedir_indice_atendimento(self):
        return int(input("Digite o NUMERO (indice): "))