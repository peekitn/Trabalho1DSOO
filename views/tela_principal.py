# Francisco

class TelaPrincipal:
    def tela_opcoes(self):
        print("--- Menu Principal ---")
        print("1 - Modulo de Pacientes")
        print("2 - Modulo de Clinicas")
        print("3 - Modulo de Relatorios")
        print("0 - Encerrar Sistema")
        opcao = int(input("Escolha a opcao: "))
        return opcao