import FreeSimpleGUI as sg

class TelaAtendimento:
    def __init__(self):
        self.__window = None
        self.init_components()
    
    # seguindo o padrao do professor nos slides
    def init_components(self):
        sg.theme('BlueMono')

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        if self.__window is not None:
            self.__window.Close()
        self.__window = None
        
    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(mensagem, title=titulo, keep_on_top=True)

    # adaptando pra nao quebrar o controlador
    def mostrar_mensagem(self, mensagem: str):
        self.show_message("[SISTEMA]", mensagem)

    def mostrar_erro(self, mensagem: str):
        self.show_message("[ERRO]", mensagem)

    # metodos da tela
    def tela_opcoes(self):
        self.init_components()
        layout = [
            [sg.Text('--- Módulo de Atendimentos ---', font=('Helvetica', 14, 'bold'), justification='center', expand_x=True)],
            [sg.HSeparator(pad=(0, 10))],
            
            [sg.Text('Atendimentos:', font=('Helvetica', 11, 'bold'))],
            [sg.Button('Agendar atendimento', key=1, size=(25, 1)), sg.Button('Listar atendimentos', key=2, size=(25, 1))],
            [sg.Button('Alterar atendimento', key=3, size=(25, 1)), sg.Button('Excluir atendimento', key=4, size=(25, 1))],
            [sg.VSeparator()],
            
            [sg.Text('Procedimentos:', font=('Helvetica', 11, 'bold'))],
            [sg.Button('Registrar procedimento', key=5, size=(25, 1)), sg.Button('Listar procedimentos', key=6, size=(25, 1))],
            [sg.Button('Alterar procedimento', key=7, size=(25, 1)), sg.Button('Remover procedimento', key=8, size=(25, 1))],
            [sg.VSeparator()],
            
            [sg.Text('Pagamentos:', font=('Helvetica', 11, 'bold'))],
            [sg.Button('Processar pagamento', key=9, size=(25, 1)), sg.Button('Listar pagamentos', key=10, size=(25, 1))],
            [sg.Button('Alterar pagamento', key=11, size=(25, 1)), sg.Button('Remover pagamento', key=12, size=(25, 1))],
            
            [sg.HSeparator(pad=(0, 15))],
            [sg.Button('Voltar', key=0, button_color=('white', '#d32f2f'), size=(12, 1), expand_x=True)]
        ]

        self.__window = sg.Window('Menu Atendimentos', layout, modal=True, element_justification='center')
        event, _ = self.open()
        self.close()
        
        return event if event is not None else 0

    def ler_dados_agendamento(self):
        self.init_components()
        layout = [
            [sg.Text('--- Dados do Agendamento ---', font=('Helvetica', 12, 'bold'))],
            [sg.Text('Data do atendimento (DD/MM/AAAA):', size=(28, 1)), sg.InputText(key='data', size=(15, 1))],
            [sg.Text('Horário de Início (HH:MM):', size=(28, 1)), sg.InputText(key='inicio', size=(10, 1))],
            [sg.Text('Horário de Término (HH:MM):', size=(28, 1)), sg.InputText(key='fim', size=(10, 1))],
            [sg.Text('Valor Base (R$):', size=(28, 1)), sg.InputText(key='valor', size=(15, 1))],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        self.__window = sg.Window('Agendar Atendimento', layout, modal=True)
        event, values = self.open()
        self.close()

        if event == 'Confirmar':
            try:
                valor_base = float(values['valor'].replace(',', '.'))
                return values['data'], values['inicio'], values['fim'], valor_base
            except ValueError:
                self.mostrar_erro("Valor Base inválido! Digite apenas números.")
                return self.ler_dados_agendamento() 
        return None, None, None, None

    def ler_dados_pagamento(self):
        self.init_components()
        layout = [
            [sg.Text('--- Registro de Pagamento ---', font=('Helvetica', 12, 'bold'))],
            [sg.Text('Modalidade:')],
            [sg.Radio('Dinheiro', "MODALIDADE", default=True, key='1'),
             sg.Radio('PIX', "MODALIDADE", key='2'),
             sg.Radio('Cartão', "MODALIDADE", key='3')],
            [sg.Text('Valor a pagar (R$):'), sg.InputText(key='valor', size=(15, 1))],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        self.__window = sg.Window('Registrar Pagamento', layout, modal=True)
        event, values = self.open()
        self.close()

        if event == 'Confirmar':
            modalidade = '1' if values['1'] else ('2' if values['2'] else '3')
            try:
                valor = float(values['valor'].replace(',', '.'))
                return modalidade, valor
            except ValueError:
                self.mostrar_erro("Valor inválido!")
                return self.ler_dados_pagamento()
        return None, None

    def ler_dados_pix(self):
        self.init_components()
        layout = [
            [sg.Text('Digite o CPF do pagador (PIX):')],
            [sg.InputText(key='cpf', size=(20, 1))],
            [sg.Button('OK')]
        ]
        
        self.__window = sg.Window('Dados PIX', layout, modal=True)
        event, values = self.open()
        self.close()
        
        return values['cpf'].strip() if event == 'OK' else ""

    def ler_dados_cartao(self):
        self.init_components()
        layout = [
            [sg.Text('Número do cartão:'), sg.InputText(key='cartao')],
            [sg.Text('Bandeira:'), sg.InputText(key='bandeira')],
            [sg.Button('OK')]
        ]
        
        self.__window = sg.Window('Dados Cartão', layout, modal=True)
        event, values = self.open()
        self.close()
        
        if event == 'OK':
            return values['cartao'].strip(), values['bandeira'].strip()
        return "", ""

    # popup para pedir dados
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
        self.init_components()
        layout = [
            [sg.Text('--- Registro de Procedimento ---', font=('Helvetica', 12, 'bold'))],
            [sg.Text('Descrição do procedimento:'), sg.InputText(key='descricao')],
            [sg.Text('Custo do procedimento (R$):'), sg.InputText(key='custo', size=(15, 1))],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        self.__window = sg.Window('Registrar Procedimento', layout, modal=True)
        event, values = self.open()
        self.close()

        if event == 'Confirmar':
            try:
                custo = float(values['custo'].replace(',', '.'))
                return values['descricao'].strip(), custo
            except ValueError:
                self.mostrar_erro("Custo inválido!")
                return self.ler_dados_procedimento()
        return None, None
