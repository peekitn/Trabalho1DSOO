from views.tela_relatorios import TelaRelatorios
from daos.atendimento_dao import AtendimentoDAO  

class ControladorRelatorios:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_relatorios = TelaRelatorios()
        self.__atendimento_dao = AtendimentoDAO()  

    def abrir_tela(self):
        self.__atendimento_dao = AtendimentoDAO()
        while True:
            opcao = self.__tela_relatorios.tela_opcoes()
            
            if opcao == 1:
                dados = self.relatorio_clinicas_mais_atendimentos()
                self.__tela_relatorios.mostrar_clinicas_mais_atendimentos(dados)
            elif opcao == 2:
                caro, barato = self.relatorio_atendimentos_extremos()
                self.__tela_relatorios.mostrar_atendimentos_extremos(caro, barato)
            elif opcao == 3:
                dados = self.relatorio_procedimentos_mais_realizados()
                self.__tela_relatorios.mostrar_procedimentos_mais_realizados(dados)
            elif opcao == 4:
                caro, barato = self.relatorio_procedimentos_extremos()
                self.__tela_relatorios.mostrar_procedimentos_extremos(caro, barato)
            elif opcao == 0:
                break
            else:
                self.__tela_relatorios.mostrar_mensagem("Opcao invalida!")

    # 1. Clínicas com maior número de atendimentos
    def relatorio_clinicas_mais_atendimentos(self):
        atendimentos = list(self.__atendimento_dao.get_all())
        
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
    def relatorio_atendimentos_extremos(self):
        atendimentos = list(self.__atendimento_dao.get_all())
        if not atendimentos:
            return None, None
            
        atendimentos_ordenados = sorted(atendimentos, key=lambda a: a.calcular_valor_total())
        mais_barato = atendimentos_ordenados[0]
        mais_caro = atendimentos_ordenados[-1]
        
        return mais_caro, mais_barato

    # 3. Procedimentos mais realizados (populares)
    def relatorio_procedimentos_mais_realizados(self):
        atendimentos = list(self.__atendimento_dao.get_all())
        contagem_procedimentos = {}
        
        for atendimento in atendimentos:
            # Usando o get_procedimentos() em vez de quebrar o encapsulamento
            for procedimento in atendimento.get_procedimentos(): 
                nome_proc = procedimento.descricao
                if nome_proc in contagem_procedimentos:
                    contagem_procedimentos[nome_proc] += 1
                else:
                    contagem_procedimentos[nome_proc] = 1
                    
        procedimentos_ordenados = sorted(contagem_procedimentos.items(), key=lambda item: item[1], reverse=True)
        return procedimentos_ordenados

    # 4. Procedimentos mais caros e mais baratos
    def relatorio_procedimentos_extremos(self):
        atendimentos = list(self.__atendimento_dao.get_all())
        todos_procedimentos = []
        
        for atendimento in atendimentos:
            todos_procedimentos.extend(atendimento.get_procedimentos())
            
        if not todos_procedimentos:
            return None, None
            
        procedimentos_ordenados = sorted(todos_procedimentos, key=lambda p: p.custo)
        mais_barato = procedimentos_ordenados[0]
        mais_caro = procedimentos_ordenados[-1]
        
        return mais_caro, mais_barato