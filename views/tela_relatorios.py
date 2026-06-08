# Francisco

class TelaRelatorios:
    def tela_opcoes(self):
        print("--- Menu de Relatorios ---")
        print("1 - Clinicas com mais atendimentos")
        print("2 - Atendimentos mais caros e mais baratos")
        print("3 - Procedimentos mais realizados")
        print("4 - Procedimentos mais caros e mais baratos")
        print("0 - Retornar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def mostrar_clinicas_mais_atendimentos(self, clinicas_ordenadas):
        print("\n--- Clinicas com Mais Atendimentos ---")
        if not clinicas_ordenadas:
            print("Nenhum atendimento registrado no sistema.")
        else:
            for clinica, quantidade in clinicas_ordenadas:
                print(f"Clinica: {clinica} | Total de Atendimentos: {quantidade}")
        print("--------------------------------------\n")

    def mostrar_atendimentos_extremos(self, mais_caro, mais_barato):
        print("\n--- Atendimentos Extremos ---")
        if mais_caro and mais_barato:
            print(f"Mais Caro: Paciente {mais_caro.paciente.nome} - Valor: R$ {mais_caro.calcular_valor_total():.2f}")
            print(f"Mais Barato: Paciente {mais_barato.paciente.nome} - Valor: R$ {mais_barato.calcular_valor_total():.2f}")
        else:
            print("Nenhum atendimento registrado no sistema.")
        print("-----------------------------\n")

    def mostrar_procedimentos_mais_realizados(self, procedimentos_ordenados):
        print("\n--- Procedimentos Mais Populares ---")
        if not procedimentos_ordenados:
            print("Nenhum procedimento registrado no sistema.")
        else:
            for procedimento, quantidade in procedimentos_ordenados:
                print(f"Procedimento: {procedimento} | Realizados: {quantidade} vezes")
        print("------------------------------------\n")

    def mostrar_procedimentos_extremos(self, mais_caro, mais_barato):
        print("\n--- Procedimentos Extremos ---")
        if mais_caro and mais_barato:
            print(f"Mais Caro: {mais_caro.descricao} - Custo: R$ {mais_caro.custo:.2f}")
            print(f"Mais Barato: {mais_barato.descricao} - Custo: R$ {mais_barato.custo:.2f}")
        else:
            print("Nenhum procedimento registrado no sistema.")
        print("------------------------------\n")
    
    def mostrar_mensagem(self, mensagem):
        print(mensagem)