# Francisco

class TelaPrincipal:
    def tela_opcoes(self):
        print("--- Menu Principal ---")
        print("1 - Modulo de Pacientes")
        print("2 - Modulo de Clinicas")
        print("3 - Modulo de Relatorios")
        print("4 - Modulo de Atendimentos")
        print("5 - Modulo de Profissionais")
        print("0 - Encerrar Sistema")
        opcao = int(input("Escolha a opcao: "))
        return opcao
    
    def mostrar_mensagem(self, mensagem: str):
        print(f"\n[SISTEMA] {mensagem}")

    def mostrar_erro(self, mensagem: str):
        print(f"\n[ERRO] {mensagem}")