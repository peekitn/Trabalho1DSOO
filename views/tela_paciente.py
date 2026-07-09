import FreeSimpleGUI as sg

class TelaPaciente:
    def __init__(self):
        self.__window = None
        self.init_components()

    # seguindo o padrao do professor nos slides
    def init_components(self):
        sg.theme('LightBlue')

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
            [sg.Text('--- Módulo de Pacientes ---', font=('Helvetica', 14, 'bold'), justification='center', expand_x=True)],
            [sg.HSeparator(pad=(0, 10))],
            [sg.Button('Cadastrar Paciente', key=1, size=(25, 1))],
            [sg.Button('Listar Pacientes', key=2, size=(25, 1))],
            [sg.Button('Alterar Paciente', key=3, size=(25, 1))],
            [sg.Button('Excluir Paciente', key=4, size=(25, 1))],
            [sg.HSeparator(pad=(0, 15))],
            [sg.Button('Voltar', key=0, button_color=('white', '#d32f2f'), size=(12, 1), expand_x=True)]
        ]

        self.__window = sg.Window('Menu Pacientes', layout, modal=True, element_justification='center')
        event, _ = self.open()
        self.close()
        
        return event if event is not None else 0

    def pegar_dados_paciente(self):
        self.init_components()
        layout = [
            [sg.Text('--- Dados do Paciente ---', font=('Helvetica', 12, 'bold'))],
            [sg.Text('Nome:', size=(28, 1)), sg.InputText(key='nome', size=(25, 1))],
            [sg.Text('CPF:', size=(28, 1)), sg.InputText(key='cpf', size=(25, 1))],
            [sg.Text('Celular:', size=(28, 1)), sg.InputText(key='celular', size=(25, 1))],
            [sg.Text('Data de Nascimento (DD/MM/AAAA):', size=(28, 1)), sg.InputText(key='data_nascimento', size=(15, 1))],
            [sg.HSeparator(pad=(0, 10))],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        self.__window = sg.Window('Cadastrar/Alterar Paciente', layout, modal=True)
        event, values = self.open()
        self.close()

        if event == 'Confirmar':
            return {
                "nome": values['nome'].strip(),
                "cpf": values['cpf'].strip(),
                "celular": values['celular'].strip(),
                "data_nascimento": values['data_nascimento'].strip()
            }
        return {"nome": "", "cpf": "", "celular": "", "data_nascimento": ""}

    def selecionar_paciente(self):
        resposta = sg.popup_get_text("Digite o CPF do paciente:", title="Selecionar Paciente")
        return resposta.strip() if resposta else ""

    def mostrar_paciente(self, dados_paciente):
        texto_exibicao = (
            f"Nome: {dados_paciente.get('nome', '')}\n"
            f"CPF: {dados_paciente.get('cpf', '')}\n"
            f"Celular: {dados_paciente.get('celular', '')}\n"
            f"Nascimento: {dados_paciente.get('data_nascimento', '')}"
        )
        self.show_message("Dados do Paciente", texto_exibicao)