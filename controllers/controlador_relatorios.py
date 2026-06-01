class ControladorRelatorios:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal

    # 1. Clínicas com maior número de atendimentos
    # Eh criado um dicionario onde varre todos os atendimentos um por um. Se a clinica do atendimento ja tiver sido contada, soma 1. Se nao tiver sido contada, inicia a contagem com 1. Depois ordena o dicionario e retorna a lista ordenada.
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
    # O lambda a: a.calcular_valor_total() diz ao Python para pegar cada atendimento e usar o resultado do cálculo do valor para organizar a fila, do menor para o maior. [0] pega o primeirão da lista (o mais barato). O [-1] é um truque para pegar o último item da lista de trás pra frente (o mais caro), sem precisar saber o tamanho exato da lista.
    def relatorio_atendimentos_extremos(self):
        atendimentos = self.__controlador_principal.atendimentos
        if not atendimentos:
            return None, None
            
        atendimentos_ordenados = sorted(atendimentos, key=lambda a: a.calcular_valor_total())
        mais_barato = atendimentos_ordenados[0]
        mais_caro = atendimentos_ordenados[-1]
        
        return mais_caro, mais_barato

    # 3. Procedimentos mais realizados (populares)
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