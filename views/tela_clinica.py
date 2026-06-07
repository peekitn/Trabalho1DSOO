class TelaClinica:
    def mostrar_mensagem(self, mensagem: str):
        print(f"\n[CLÍNICA] {mensagem}")

    def mostrar_erro(self, mensagem: str):
        print(f"\n[ERRO - CLÍNICA] {mensagem}")

    def ler_dados_clinica(self):
        print("\n Cadastro de Clínica ")
        nome = input("Nome da Clínica: ").strip()
        cidade = input("Cidade: ").strip()
        descricao = input("Descrição: ").strip()
        return nome, cidade, descricao
