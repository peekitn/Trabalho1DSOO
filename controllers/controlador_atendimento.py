from views.tela_atendimento import TelaAtendimento
from datetime import datetime, date
from models.atendimento import Atendimento, TipoAtendimento, Procedimento, MenorDeIdadeException, ForaDoHorarioComercialException, PagamentoAtrasadoException, ValorInvalidoException
from models.pagamentos import PagamentoDinheiro, PagamentoPix, PagamentoCartao


class ControladorAtendimento:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__view = TelaAtendimento() 

    def _validar_idade_paciente(self, paciente, data_atendimento):
        data_nasc = paciente.data_nascimento
        idade = data_atendimento.year - data_nasc.year - ((data_atendimento.month, data_atendimento.day) < (data_nasc.month, data_nasc.day))
        
        if idade < 18:
            raise MenorDeIdadeException()

    def _validar_horario_clinica(self, horario_inicio: str):
        hora = int(horario_inicio.split(":")[0])
        if hora < 8 or hora >= 18:
            raise ForaDoHorarioComercialException()

    def agendar_atendimento(self, clinica, paciente, profissional, tipo_atendimento):
        try:
            data_str, h_inicio, h_fim, valor_base = self.__view.ler_dados_agendamento()
            data_atendimento = datetime.strptime(data_str, "%d/%m/%Y").date()

            self._validar_idade_paciente(paciente, data_atendimento)
            self._validar_horario_clinica(h_inicio)

            novo_atendimento = Atendimento(
                data_atendimento=data_atendimento,
                horario_inicio=h_inicio,
                horario_fim=h_fim,
                valor_base=valor_base,
                clinica=clinica,
                paciente=paciente,
                profissional=profissional,
                tipo=tipo_atendimento
            )

            self.__controlador_principal.atendimentos.append(novo_atendimento)
            self.__view.mostrar_mensagem("Atendimento agendado com sucesso!")
            return novo_atendimento

        except ValueError:
            self.__view.mostrar_erro("Formato de data ou numero invalido inserido.")
        except (MenorDeIdadeException, ForaDoHorarioComercialException) as e:
            self.__view.mostrar_erro(str(e))
        except Exception as e:
            self.__view.mostrar_erro(f"Erro inesperado: {str(e)}")

    def processar_pagamento(self, atendimento):
        try:
            self.__view.mostrar_mensagem(f"Valor restante: R$ {atendimento.calcular_valor_restante():.2f}")
            modalidade, valor = self.__view.ler_dados_pagamento()
            
            data_hoje = date.today()
            novo_pagamento = None

            if modalidade == '1':
                novo_pagamento = PagamentoDinheiro(data_hoje, atendimento.paciente, valor)
            elif modalidade == '2':
                cpf = self.__view.ler_dados_pix() 
                novo_pagamento = PagamentoPix(data_hoje, atendimento.paciente, valor, cpf)
            elif modalidade == '3':
                cartao, bandeira = self.__view.ler_dados_cartao() 
                novo_pagamento = PagamentoCartao(data_hoje, atendimento.paciente, valor, cartao, bandeira)
            else:
                self.__view.mostrar_erro("Modalidade invalida.")
                return

            atendimento.registrar_pagamento(novo_pagamento)
            self.__view.mostrar_mensagem(f"Pagamento de R$ {valor:.2f} registrado. Restante: R$ {atendimento.calcular_valor_restante():.2f}")

        except (PagamentoAtrasadoException, ValorInvalidoException) as e:
            self.__view.mostrar_erro(str(e))

    def abrir_tela(self):
        while True:
            try:
                opcao = self.__view.tela_opcoes()
                
                if opcao == 1:
                    self._iniciar_agendamento()
                elif opcao == 2:
                    self._listar_atendimentos()
                elif opcao == 3:
                    self._alterar_atendimento()
                elif opcao == 4:    
                    self._excluir_atendimento()
                elif opcao == 5:
                    self._iniciar_registro_procedimento()
                elif opcao == 6:
                    self._listar_procedimentos()
                elif opcao == 7:
                    self._alterar_procedimento()
                elif opcao == 8:
                    self._excluir_procedimento()
                elif opcao == 9:
                    self._iniciar_pagamento()
                elif opcao == 10:
                    self._listar_pagamentos()
                elif opcao == 11:
                    self._alterar_pagamento()
                elif opcao == 12:
                    self._excluir_pagamento()
                elif opcao == 0:
                    break
                else:
                    self.__view.mostrar_erro("Opcao invalida.")
            except ValueError:
                self.__view.mostrar_erro("Digite um numero valido.")

    def _iniciar_agendamento(self):
        if not self.__controlador_principal.pacientes:
            self.__view.mostrar_erro("Cadastre um paciente primeiro.")
            return
        if not self.__controlador_principal.clinicas:
            self.__view.mostrar_erro("Cadastre uma clinica primeiro.")
            return
        if not self.__controlador_principal.profissionais:
            self.__view.mostrar_erro("Cadastre um profissional primeiro.")
            return

        cpf_paciente = self.__view.pedir_cpf_paciente()
        paciente = next((p for p in self.__controlador_principal.pacientes if p.cpf == cpf_paciente), None)
        if not paciente:
            self.__view.mostrar_erro("Paciente nao encontrado.")
            return

        cpf_prof = self.__view.pedir_cpf_profissional()
        profissional = next((p for p in self.__controlador_principal.profissionais if p.cpf == cpf_prof), None)
        if not profissional:
            self.__view.mostrar_erro("Profissional nao encontrado.")
            return

        nome_clinica = self.__view.pedir_nome_clinica()
        clinica = next((c for c in self.__controlador_principal.clinicas if c.nome.lower() == nome_clinica.lower()), None)
        if not clinica:
            self.__view.mostrar_erro("Clinica nao encontrada.")
            return
        nome_tipo = self.__view.pedir_tipo_atendimento()
        tipo = TipoAtendimento(nome_tipo)

        self.agendar_atendimento(clinica, paciente, profissional, tipo)

    def _iniciar_pagamento(self):
        if not self.__controlador_principal.atendimentos:
            self.__view.mostrar_erro("Nenhum atendimento registrado no sistema.")
            return

        self.__view.mostrar_mensagem("Atendimentos Disponíveis:")
        for i, at in enumerate(self.__controlador_principal.atendimentos):
            self.__view.mostrar_mensagem(f"[{i}] Paciente: {at.paciente.nome} | Restante a Pagar: R$ {at.calcular_valor_restante():.2f}")

        try:
            indice = self.__view.pedir_indice_atendimento()
            atendimento_selecionado = self.__controlador_principal.atendimentos[indice]
            
            if atendimento_selecionado.calcular_valor_restante() <= 0:
                self.__view.mostrar_erro("Este atendimento ja esta totalmente pago!")
                return
                
            self.processar_pagamento(atendimento_selecionado)
        except (IndexError, ValueError):
            self.__view.mostrar_erro("Indice invalido.")

    def _iniciar_registro_procedimento(self):
        if not self.__controlador_principal.atendimentos:
            self.__view.mostrar_erro("Nenhum atendimento registrado no sistema.")
            return

        self.__view.mostrar_mensagem("Atendimentos Disponíveis para Procedimentos:")
        for i, at in enumerate(self.__controlador_principal.atendimentos):
            self.__view.mostrar_mensagem(f"[{i}] Paciente: {at.paciente.nome} | Clinica: {at.clinica.nome}")

        try:
            indice = self.__view.pedir_indice_atendimento()
            atendimento_selecionado = self.__controlador_principal.atendimentos[indice]
            
            descricao, custo = self.__view.ler_dados_procedimento()
            novo_procedimento = Procedimento(descricao, custo, atendimento_selecionado.profissional)
            
            atendimento_selecionado.adicionar_procedimento(novo_procedimento)
            self.__view.mostrar_mensagem("Procedimento registrado com sucesso!")

        except (IndexError, ValueError):
            self.__view.mostrar_erro("Indice ou valor invalido.")

    def _listar_atendimentos(self):
        if not self.__controlador_principal.atendimentos:
            self.__view.mostrar_erro("Nenhum atendimento registrado.")
            return False
        
        self.__view.mostrar_mensagem("Lista de Atendimentos:")
        for i, at in enumerate(self.__controlador_principal.atendimentos):
            self.__view.mostrar_mensagem(f"[{i}] {at.data_atendimento.strftime('%d/%m/%Y')} - Paciente: {at.paciente.nome} | Profissional: {at.profissional.nome} | Clinica: {at.clinica.nome}")
        return True

    def _alterar_atendimento(self):
        if not self._listar_atendimentos(): return
        try:
            self.__view.mostrar_mensagem("Qual atendimento deseja alterar?")
            indice = self.__view.pedir_indice_atendimento()
            at = self.__controlador_principal.atendimentos[indice]
            
            self.__view.mostrar_mensagem("Digite os novos dados (IDs e Tipo nao mudam):")
            data_str, h_inicio, h_fim, valor_base = self.__view.ler_dados_agendamento()
            data_atendimento = datetime.strptime(data_str, "%d/%m/%Y").date()
            
            self._validar_horario_clinica(h_inicio)
            
            at.data_atendimento = data_atendimento
            at.horario_inicio = h_inicio
            at.horario_fim = h_fim
            at.valor_base = valor_base
            self.__view.mostrar_mensagem("Atendimento alterado com sucesso!")
        except (IndexError, ValueError):
            self.__view.mostrar_erro("Indice ou formato de data invalido.")
        except ForaDoHorarioComercialException as e:
            self.__view.mostrar_erro(str(e))

    def _excluir_atendimento(self):
        if not self._listar_atendimentos(): return
        try:
            self.__view.mostrar_mensagem("Qual atendimento deseja excluir?")
            indice = self.__view.pedir_indice_atendimento()
            self.__controlador_principal.atendimentos.pop(indice)
            self.__view.mostrar_mensagem("Atendimento excluido com sucesso!")
        except (IndexError, ValueError):
            self.__view.mostrar_erro("Indice invalido.")

    def _excluir_procedimento(self):
        if not self._listar_atendimentos(): return
        try:
            self.__view.mostrar_mensagem("De qual atendimento deseja remover o procedimento?")
            ind_at = self.__view.pedir_indice_atendimento()
            at = self.__controlador_principal.atendimentos[ind_at]
            
            procs = at.get_procedimentos()
            if not procs:
                self.__view.mostrar_erro("Sem procedimentos neste atendimento.")
                return
                
            for i, p in enumerate(procs):
                self.__view.mostrar_mensagem(f"[{i}] {p.descricao} - R$ {p.custo}")
                
            self.__view.mostrar_mensagem("Qual procedimento deseja excluir?")
            ind_proc = self.__view.pedir_indice_atendimento()
            at.remover_procedimento(procs[ind_proc])
            self.__view.mostrar_mensagem("Procedimento removido!")
        except (IndexError, ValueError):
            self.__view.mostrar_erro("Indice invalido.")

    def _excluir_pagamento(self):
        if not self._listar_atendimentos(): return
        try:
            self.__view.mostrar_mensagem("De qual atendimento deseja remover o pagamento?")
            ind_at = self.__view.pedir_indice_atendimento()
            at = self.__controlador_principal.atendimentos[ind_at]
            
            pags = at.get_pagamentos()
            if not pags:
                self.__view.mostrar_erro("Sem pagamentos neste atendimento.")
                return
                
            for i, p in enumerate(pags):
                self.__view.mostrar_mensagem(f"[{i}] R$ {p.valor_pago} em {p.data.strftime('%d/%m/%Y')}")
                
            self.__view.mostrar_mensagem("Qual pagamento deseja excluir?")
            ind_pag = self.__view.pedir_indice_atendimento()
            at.remover_pagamento(pags[ind_pag])
            self.__view.mostrar_mensagem("Pagamento removido!")
        except (IndexError, ValueError):
            self.__view.mostrar_erro("Indice invalido.")

    def _listar_procedimentos(self):
        if not self._listar_atendimentos(): return
        try:
            self.__view.mostrar_mensagem("De qual atendimento deseja listar os procedimentos?")
            ind_at = self.__view.pedir_indice_atendimento()
            at = self.__controlador_principal.atendimentos[ind_at]
            procs = at.get_procedimentos()
            if not procs:
                self.__view.mostrar_erro("Sem procedimentos neste atendimento.")
            else:
                self.__view.mostrar_mensagem("--- Procedimentos do Atendimento ---")
                for i, p in enumerate(procs):
                    self.__view.mostrar_mensagem(f"[{i}] {p.descricao} - R$ {p.custo:.2f}")
        except (IndexError, ValueError):
            self.__view.mostrar_erro("Indice invalido.")

    def _alterar_procedimento(self):
        if not self._listar_atendimentos(): return
        try:
            self.__view.mostrar_mensagem("De qual atendimento deseja alterar o procedimento?")
            ind_at = self.__view.pedir_indice_atendimento()
            at = self.__controlador_principal.atendimentos[ind_at]
            procs = at.get_procedimentos()
            if not procs:
                self.__view.mostrar_erro("Sem procedimentos neste atendimento.")
                return
            for i, p in enumerate(procs):
                self.__view.mostrar_mensagem(f"[{i}] {p.descricao} - R$ {p.custo:.2f}")
            
            self.__view.mostrar_mensagem("Qual procedimento deseja alterar?")
            ind_proc = self.__view.pedir_indice_atendimento()
            proc_selecionado = procs[ind_proc]
            
            descricao, custo = self.__view.ler_dados_procedimento()
            proc_selecionado.descricao = descricao
            proc_selecionado.custo = custo
            self.__view.mostrar_mensagem("Procedimento alterado com sucesso!")
        except (IndexError, ValueError):
            self.__view.mostrar_erro("Indice ou valor invalido.")

    def _listar_pagamentos(self):
        if not self._listar_atendimentos(): return
        try:
            self.__view.mostrar_mensagem("De qual atendimento deseja listar os pagamentos?")
            ind_at = self.__view.pedir_indice_atendimento()
            at = self.__controlador_principal.atendimentos[ind_at]
            pags = at.get_pagamentos()
            if not pags:
                self.__view.mostrar_erro("Sem pagamentos neste atendimento.")
            else:
                self.__view.mostrar_mensagem("--- Pagamentos do Atendimento ---")
                for i, p in enumerate(pags):
                    self.__view.mostrar_mensagem(f"[{i}] R$ {p.valor_pago:.2f} em {p.data.strftime('%d/%m/%Y')}")
        except (IndexError, ValueError):
            self.__view.mostrar_erro("Indice invalido.")

    def _alterar_pagamento(self):
        if not self._listar_atendimentos(): return
        try:
            self.__view.mostrar_mensagem("De qual atendimento deseja alterar o pagamento?")
            ind_at = self.__view.pedir_indice_atendimento()
            at = self.__controlador_principal.atendimentos[ind_at]
            pags = at.get_pagamentos()
            if not pags:
                self.__view.mostrar_erro("Sem pagamentos neste atendimento.")
                return
            for i, p in enumerate(pags):
                self.__view.mostrar_mensagem(f"[{i}] R$ {p.valor_pago:.2f} em {p.data.strftime('%d/%m/%Y')}")
            
            self.__view.mostrar_mensagem("Qual pagamento deseja alterar?")
            ind_pag = self.__view.pedir_indice_atendimento()
            pag_selecionado = pags[ind_pag]
            
            # Reutilizando a tela de pagamento para atualizar apenas o valor
            modalidade, valor = self.__view.ler_dados_pagamento()
            pag_selecionado.valor_pago = valor
            self.__view.mostrar_mensagem("Valor do pagamento alterado com sucesso!")
        except (IndexError, ValueError):
            self.__view.mostrar_erro("Indice ou valor invalido.")