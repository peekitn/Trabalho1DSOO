class TelaPaciente:
    def tela_opcoes(self):
        print("\n--- Modulo de Pacientes ---")
        print("1 - Cadastrar Paciente")
        print("2 - Listar Pacientes")
        print("3 - Alterar Paciente")
        print("4 - Excluir Paciente")
        print("0 - Voltar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pegar_dados_paciente(self):
        print("\n--- Dados do Paciente ---")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        celular = input("Celular: ")
        data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
        return {"nome": nome, "cpf": cpf, "celular": celular, "data_nascimento": data_nascimento}

    def selecionar_paciente(self):
        return input("Digite o CPF do paciente: ")

    def mostrar_paciente(self, dados_paciente):
        print(f"Nome: {dados_paciente['nome']} | CPF: {dados_paciente['cpf']} | Celular: {dados_paciente['celular']} | Nasc: {dados_paciente['data_nascimento']}")

    def mostrar_mensagem(self, mensagem):
        print(f"\n[SISTEMA] {mensagem}")

    def mostrar_erro(self, mensagem):
        print(f"\n[ERRO] {mensagem}")