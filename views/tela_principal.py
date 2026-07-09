import FreeSimpleGUI as sg

class TelaPrincipal:
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
            [sg.Text('--- Sistema de Gestão Médica ---', font=('Helvetica', 16, 'bold'), justification='center', expand_x=True)],
            [sg.Text('Menu Principal', font=('Helvetica', 12), justification='center', expand_x=True)],
            [sg.HSeparator(pad=(0, 15))],
            
            [sg.Button('Pacientes', key=1, size=(30, 2))],
            [sg.Button('Clínicas', key=2, size=(30, 2))],
            [sg.Button('Relatórios', key=3, size=(30, 2))],
            [sg.Button('Atendimentos', key=4, size=(30, 2))],
            [sg.Button('Profissionais', key=5, size=(30, 2))],
            
            [sg.HSeparator(pad=(0, 15))],
            [sg.Button('Encerrar Sistema', key=0, button_color=('white', '#d32f2f'), size=(15, 1), expand_x=True)]
        ]

        self.__window = sg.Window('Menu Principal', layout, element_justification='center')
        
        event, _ = self.open()
        
        self.close()
        
        return event if event is not None else 0