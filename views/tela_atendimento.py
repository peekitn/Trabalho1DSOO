import FreeSimpleGUI as sg

class TelaAtendimento:
    def __init__(self):
        self.__window = None
        self.init_components()
    
    def init_components(self):
        sg.theme('LightBlue')

    def mostrar_mensagem(self, mensagem: str):
        sg.popup_ok(mensagem, title="[SISTEMA]", keep_on_top=True)

    def mostrar_erro(self, mensagem: str):
        sg.popup_error(mensagem, title="[ERRO]", keep_on_top=True)

    def tela_opcoes(self):

        layout = [
            [sg.Text('--- Módulo de Atendimentos ---', font=('Helvetica', 14, 'bold'), justification='center', expand_x=True)],
            [sg.HSeparator(pad=(0, 10))],
            
            # Seção de Atendimentos
            [sg.Text('Atendimentos:', font=('Helvetica', 11, 'bold'))],
            [sg.Button('Agendar atendimento', key=1, size=(25, 1)), sg.Button('Listar atendimentos', key=2, size=(25, 1))],
            [sg.Button('Alterar atendimento', key=3, size=(25, 1)), sg.Button('Excluir atendimento', key=4, size=(25, 1))],
            [sg.VSeparator()],
            
            # Seção de Procedimentos
            [sg.Text('Procedimentos:', font=('Helvetica', 11, 'bold'))],
            [sg.Button('Registrar procedimento', key=5, size=(25, 1)), sg.Button('Listar procedimentos', key=6, size=(25, 1))],
            [sg.Button('Alterar procedimento', key=7, size=(25, 1)), sg.Button('Remover procedimento', key=8, size=(25, 1))],
            [sg.VSeparator()],
            
            # Seção de Pagamentos
            [sg.Text('Pagamentos:', font=('Helvetica', 11, 'bold'))],
            [sg.Button('Processar pagamento', key=9, size=(25, 1)), sg.Button('Listar pagamentos', key=10, size=(25, 1))],
            [sg.Button('Alterar pagamento', key=11, size=(25, 1)), sg.Button('Remover pagamento', key=12, size=(25, 1))],
            
            [sg.HSeparator(pad=(0, 15))],
            [sg.Button('Voltar', key=0, button_color=('white', '#d32f2f'), size=(12, 1), expand_x=True)]
        ]

        window = sg.Window('Menu Atendimentos', layout, modal=True, element_justification='center')
        event, _ = window.read()
        window.close()
        
        # Se o usuário fechar o X da janela, retorna 0 (Voltar) para evitar quebra no Controller
        return event if event is not None else 0

    def ler_dados_agendamento(self):
        #Abre formulário para coletar dados do agendamento.
        layout = [
            [sg.Text('--- Dados do Agendamento ---', font=('Helvetica', 12, 'bold'))],
            [sg.Text('Data do atendimento (DD/MM/AAAA):', size=(28, 1)), sg.InputText(key='data', size=(15, 1))],
            [sg.Text('Horário de Início (HH:MM):', size=(28, 1)), sg.InputText(key='inicio', size=(10, 1))],
            [sg.Text('Horário de Término (HH:MM):', size=(28, 1)), sg.InputText(key='fim', size=(10, 1))],
            [sg.Text('Valor Base (R$):', size=(28, 1)), sg.InputText(key='valor', size=(15, 1))],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Agendar Atendimento', layout, modal=True)
        event, values = window.read()
        window.close()

        if event == 'Confirmar':
            try:
                valor_base = float(values['valor'].replace(',', '.'))
                return values['data'], values['inicio'], values['fim'], valor_base
            except ValueError:
                self.mostrar_erro("Valor Base inválido! Digite apenas números.")
                return self.ler_dados_agendamento() # Tenta novamente se o float falhar
        return None, None, None, None

    def ler_dados_pagamento(self):
        layout = [
            [sg.Text('--- Registro de Pagamento ---', font=('Helvetica', 12, 'bold'))],
            [sg.Text('Modalidade:')],
            [sg.Radio('Dinheiro', "MODALIDADE", default=True, key='1'),
             sg.Radio('PIX', "MODALIDADE", key='2'),
             sg.Radio('Cartão', "MODALIDADE", key='3')],
            [sg.Text('Valor a pagar (R$):'), sg.InputText(key='valor', size=(15, 1))],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Registrar Pagamento', layout, modal=True)
        event, values = window.read()
        window.close()

        if event == 'Confirmar':
            # Identifica qual botão foi selecionado
            modalidade = '1' if values['1'] else ('2' if values['2'] else '3')
            try:
                valor = float(values['valor'].replace(',', '.'))
                return modalidade, valor
            except ValueError:
                self.mostrar_erro("Valor inválido!")
                return self.ler_dados_pagamento()
        return None, None

    def ler_dados_pix(self):

        layout = [
            [sg.Text('Digite o CPF do pagador (PIX):')],
            [sg.InputText(key='cpf', size=(20, 1))],
            [sg.Button('OK')]
        ]
        window = sg.Window('Dados PIX', layout, modal=True)
        event, values = window.read()
        window.close()
        return values['cpf'].strip() if event == 'OK' else ""

    def ler_dados_cartao(self):

        layout = [
            [sg.Text('Número do cartão:'), sg.InputText(key='cartao')],
            [sg.Text('Bandeira:'), sg.InputText(key='bandeira')],
            [sg.Button('OK')]
        ]
        window = sg.Window('Dados Cartão', layout, modal=True)
        event, values = window.read()
        window.close()
        if event == 'OK':
            return values['cartao'].strip(), values['bandeira'].strip()
        return "", ""

    def pedir_cpf_paciente(self):
        resposta = sg.popup_get_text("Digite o CPF do Paciente:", title="Paciente")
        return resposta.strip() if resposta else ""

    def pedir_cpf_profissional(self):
        resposta = sg.popup_get_text("Digite o CPF do Profissional:", title="Profissional")
        return resposta.strip() if resposta else ""

    def pedir_nome_clinica(self):
        resposta = sg.popup_get_text("Digite o Nome da Clínica:", title="Clínica")
        return resposta.strip() if resposta else ""

    def pedir_tipo_atendimento(self):
        resposta = sg.popup_get_text("Tipo de Atendimento (Ex: Consulta, Exame):", title="Atendimento")
        return resposta.strip() if resposta else ""

    def pedir_indice(self, mensagem):
        resposta = sg.popup_get_text(mensagem, title="Selecionar Índice")
        try:
            return int(resposta) if resposta else None
        except ValueError:
            self.mostrar_erro("Índice deve ser um número inteiro!")
            return self.pedir_indice(mensagem)

    def pedir_indice_atendimento(self):
        return self.pedir_indice("Digite o NÚMERO (índice):")

    def ler_dados_procedimento(self):
        """Formulário para preencher o procedimento."""
        layout = [
            [sg.Text('--- Registro de Procedimento ---', font=('Helvetica', 12, 'bold'))],
            [sg.Text('Descrição do procedimento:'), sg.InputText(key='descricao')],
            [sg.Text('Custo do procedimento (R$):'), sg.InputText(key='custo', size=(15, 1))],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Registrar Procedimento', layout, modal=True)
        event, values = window.read()
        window.close()

        if event == 'Confirmar':
            try:
                custo = float(values['custo'].replace(',', '.'))
                return values['descricao'].strip(), custo
            except ValueError:
                self.mostrar_erro("Custo inválido!")
                return self.ler_dados_procedimento()
        return None, None
    
    def open(self):
        button, values = self._window.Read()
        return button, values
    
    def close(self):
        self._window.Close()
        
    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
