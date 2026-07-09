import FreeSimpleGUI as sg

class TelaProfissional:
    def __init__(self):
        self.__window = None
        self.init_components()

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

    def mostrar_mensagem(self, mensagem: str):
        self.show_message("[SISTEMA]", mensagem)

    def mostrar_erro(self, mensagem: str):
        self.show_message("[ERRO]", mensagem)

    def tela_opcoes(self):
        self.init_components()
        layout = [
            [sg.Text('--- Módulo de Profissionais ---', font=('Helvetica', 14, 'bold'), justification='center', expand_x=True)],
            [sg.HSeparator(pad=(0, 10))],
            
            [sg.Button('Cadastrar Profissional', key=1, size=(25, 1))],
            [sg.Button('Listar Profissionais', key=2, size=(25, 1))],
            [sg.Button('Alterar Profissional', key=4, size=(25, 1))],
            [sg.Button('Excluir Profissional', key=3, size=(25, 1))],
            
            [sg.HSeparator(pad=(0, 15))],
            [sg.Button('Voltar', key=0, button_color=('white', '#d32f2f'), size=(12, 1), expand_x=True)]
        ]

        self.__window = sg.Window('Menu Profissionais', layout, modal=True, element_justification='center')
        
        event, _ = self.open()
        
        self.close()
        
        return event if event is not None else 0

    def ler_dados_profissional(self):
        self.init_components()
        layout = [
            [sg.Text('--- Dados do Profissional ---', font=('Helvetica', 12, 'bold'))],
            [sg.Text('Nome:', size=(25, 1)), sg.InputText(key='nome', size=(30, 1))],
            [sg.Text('Celular:', size=(25, 1)), sg.InputText(key='celular', size=(30, 1))],
            [sg.Text('CPF (apenas números):', size=(25, 1)), sg.InputText(key='cpf', size=(30, 1))],
            [sg.Text('Especialidade:', size=(25, 1)), sg.InputText(key='especialidade', size=(30, 1))],
            [sg.Text('Registro (Ex: CRM):', size=(25, 1)), sg.InputText(key='registro', size=(30, 1))],
            [sg.HSeparator(pad=(0, 10))],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        self.__window = sg.Window('Dados do Profissional', layout, modal=True)
        event, values = self.open()
        self.close()

        if event == 'Confirmar':
            return (
                values['nome'].strip(),
                values['celular'].strip(),
                values['cpf'].strip(),
                values['especialidade'].strip(),
                values['registro'].strip()
            )
        
        return "", "", "", "", ""

    def mostrar_profissional(self, nome, cpf, especialidade, registro):
        texto = f"Profissional: {nome}\nCPF: {cpf}\nEspecialidade: {especialidade}\nRegistro: {registro}"
        self.show_message("Dados do Profissional", texto)

    def ler_dado_exclusao(self):
        resposta = sg.popup_get_text("Digite o CPF do profissional:", title="Buscar Profissional")
        return resposta.strip() if resposta else ""