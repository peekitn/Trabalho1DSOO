class TelaClinica:
    def tela_opcoes(self):
        print("\n--- Modulo de Clinicas ---")
        print("1 - Cadastrar Clinica")
        print("2 - Listar Clinicas")
        print("3 - Excluir Clinica")
        print("4 - Alterar Clinica")
        print("0 - Voltar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def mostrar_mensagem(self, mensagem: str):
        print(f"\n[SISTEMA] {mensagem}")

    def mostrar_erro(self, mensagem: str):
        print(f"\n[ERRO] {mensagem}")

    def ler_dados_clinica(self):
        print("\n--- Dados da Clinica ---")
        nome = input("Nome da Clinica: ").strip()
        cidade = input("Cidade: ").strip()
        descricao = input("Descricao: ").strip()
        return nome, cidade, descricao

    def mostrar_clinica(self, nome: str, cidade: str):
        print(f"- {nome} ({cidade})")

    def ler_dados_exclusao(self):
        print("\n--- Buscar Clinica ---")
        nome = input("Nome da Clinica: ").strip()
        cidade = input("Cidade da Clinica: ").strip()
        return nome, cidade