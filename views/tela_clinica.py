import FreeSimpleGUI as sg

class TelaClinica:
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
            [sg.Text('--- Módulo de Clínicas ---', font=('Helvetica', 14, 'bold'), justification='center', expand_x=True)],
            [sg.HSeparator(pad=(0, 10))],
            [sg.Button('Cadastrar Clínica', key=1, size=(25, 1))],
            [sg.Button('Listar Clínicas', key=2, size=(25, 1))],
            [sg.Button('Alterar Clínica', key=4, size=(25, 1))],
            [sg.Button('Excluir Clínica', key=3, size=(25, 1))],
            [sg.HSeparator(pad=(0, 15))],
            [sg.Button('Voltar', key=0, button_color=('white', '#d32f2f'), size=(12, 1), expand_x=True)]
        ]

        self.__window = sg.Window('Menu Clínicas', layout, modal=True, element_justification='center')
        event, _ = self.open()
        self.close()
        
        return event if event is not None else 0

    def ler_dados_clinica(self):
        self.init_components()
        layout = [
            [sg.Text('--- Dados da Clínica ---', font=('Helvetica', 12, 'bold'))],
            [sg.Text('Nome da Clínica:', size=(15, 1)), sg.InputText(key='nome', size=(30, 1))],
            [sg.Text('Cidade:', size=(15, 1)), sg.InputText(key='cidade', size=(30, 1))],
            [sg.Text('Descrição:', size=(15, 1)), sg.InputText(key='descricao', size=(30, 1))],
            [sg.HSeparator(pad=(0, 10))],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        self.__window = sg.Window('Dados da Clínica', layout, modal=True)
        event, values = self.open()
        self.close()

        if event == 'Confirmar':
            return values['nome'].strip(), values['cidade'].strip(), values['descricao'].strip()
        
        return "", "", ""

    def mostrar_clinica(self, nome: str, cidade: str):
        self.show_message("Informações da Clínica", f"Clínica: {nome}\nCidade: {cidade}")

    def ler_dados_exclusao(self):
        self.init_components()
        layout = [
            [sg.Text('--- Buscar Clínica ---', font=('Helvetica', 12, 'bold'))],
            [sg.Text('Nome da Clínica:', size=(15, 1)), sg.InputText(key='nome', size=(30, 1))],
            [sg.Text('Cidade da Clínica:', size=(15, 1)), sg.InputText(key='cidade', size=(30, 1))],
            [sg.HSeparator(pad=(0, 10))],
            [sg.Button('Buscar'), sg.Button('Cancelar')]
        ]

        self.__window = sg.Window('Buscar Clínica', layout, modal=True)
        event, values = self.open()
        self.close()

        if event == 'Buscar':
            return values['nome'].strip(), values['cidade'].strip()
        return "", ""
