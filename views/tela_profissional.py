class TelaProfissional:
    def mostrar_mensagem(self, mensagem: str):
        print(f"\n[PROFISSIONAL] {mensagem}")

    def mostrar_erro(self, mensagem: str):
        print(f"\n[ERRO - PROFISSIONAL] {mensagem}")

    def ler_dados_profissional(self):
        print("\n Cadastro de Profissional de Saúde ")
        nome = input("Nome: ").strip()
        celular = input("Celular: ").strip()
        cpf = input("CPF (apenas números): ").strip()
        especialidade = input("Especialidade: ").strip()
        registro = input("Registro Profissional (Ex: CRM): ").strip()
        return nome, celular, cpf, especialidade, registro