class ControladorRelatorios:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal

    # 1. Clínicas com maior número de atendimentos
    # Cria um dicionário para contar as ocorrências varrendo a lista de atendimentos. Se a clínica já existe no dicionário, soma +1; se não, inicia em 1. Por fim, ordena os dados do maior para o menor com base na quantidade de consultas e retorna a lista.
    def relatorio_clinicas_mais_atendimentos(self):
        atendimentos = self.__controlador_principal.atendimentos
        contagem_clinicas = {}
        
        for atendimento in atendimentos:
            nome_clinica = atendimento.clinica.nome
            if nome_clinica in contagem_clinicas:
                contagem_clinicas[nome_clinica] += 1
            else:
                contagem_clinicas[nome_clinica] = 1
                
        clinicas_ordenadas = sorted(contagem_clinicas.items(), key=lambda item: item[1], reverse=True)
        return clinicas_ordenadas

    # 2. Atendimentos mais caros e mais baratos
    # Ordena a lista de atendimentos com base no valor total calculado, organizando do menor para o maior. Retorna diretamente os extremos dessa fila ordenada usando os índices [0] para capturar o atendimento mais barato e [-1] para capturar o mais caro.
    def relatorio_atendimentos_extremos(self):
        atendimentos = self.__controlador_principal.atendimentos
        if not atendimentos:
            return None, None
            
        atendimentos_ordenados = sorted(atendimentos, key=lambda a: a.calcular_valor_total())
        mais_barato = atendimentos_ordenados[0]
        mais_caro = atendimentos_ordenados[-1]
        
        return mais_caro, mais_barato

    # 3. Procedimentos mais realizados (populares)
    # Acessa a lista encapsulada de procedimentos de cada atendimento e utiliza um dicionário para contabilizar a frequência de execução de cada um. Em seguida, ordena a contagem em ordem decrescente para retornar os procedimentos mais populares no topo.
    def relatorio_procedimentos_mais_realizados(self):
        atendimentos = self.__controlador_principal.atendimentos
        contagem_procedimentos = {}
        
        for atendimento in atendimentos:
            # Aqui acessa a lista encapsulada 
            for procedimento in atendimento._Atendimento__procedimentos: 
                nome_proc = procedimento.descricao
                if nome_proc in contagem_procedimentos:
                    contagem_procedimentos[nome_proc] += 1
                else:
                    contagem_procedimentos[nome_proc] = 1
                    
        procedimentos_ordenados = sorted(contagem_procedimentos.items(), key=lambda item: item[1], reverse=True)
        return procedimentos_ordenados

    # 4. Procedimentos mais caros e mais baratos
    # Extrai todos os procedimentos de todos os atendimentos para dentro de uma única lista consolidada utilizando o comando 'extend'. Depois, ordena essa lista geral pelo valor de custo e retorna os itens das extremidades [0] e [-1] representando o mais barato e o mais caro.
    def relatorio_procedimentos_extremos(self):
        atendimentos = self.__controlador_principal.atendimentos
        todos_procedimentos = []
        
        for atendimento in atendimentos:
            todos_procedimentos.extend(atendimento._Atendimento__procedimentos)
            
        if not todos_procedimentos:
            return None, None
            
        procedimentos_ordenados = sorted(todos_procedimentos, key=lambda p: p.custo)
        mais_barato = procedimentos_ordenados[0]
        mais_caro = procedimentos_ordenados[-1]
        
        return mais_caro, mais_barato