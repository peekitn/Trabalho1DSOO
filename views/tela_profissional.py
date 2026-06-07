class TelaProfissional:
    def tela_opcoes(self):
        print("\n--- Modulo de Profissionais ---")
        print("1 - Cadastrar Profissional")
        print("2 - Listar Profissionais")
        print("0 - Voltar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def mostrar_mensagem(self, mensagem: str):
        print(f"\n[SISTEMA] {mensagem}")

    def mostrar_erro(self, mensagem: str):
        print(f"\n[ERRO] {mensagem}")

    def ler_dados_profissional(self):
        print("\n--- Cadastro de Profissional ---")
        nome = input("Nome: ").strip()
        celular = input("Celular: ").strip()
        cpf = input("CPF (apenas numeros): ").strip()
        especialidade = input("Especialidade: ").strip()
        registro = input("Registro Profissional (Ex: CRM): ").strip()
        return nome, celular, cpf, especialidade, registro

    def mostrar_profissional(self, nome, cpf, especialidade, registro):
        print(f"- {nome} | CPF: {cpf} | Especialidade: {especialidade} | Reg: {registro}")