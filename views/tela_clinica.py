import FreeSimpleGUI as sg

class TelaClinica:
    def __init__(self):
        sg.theme('LightBlue')

    def mostrar_mensagem(self, mensagem: str):
        sg.popup_ok(mensagem, title="[SISTEMA]", keep_on_top=True)

    def mostrar_erro(self, mensagem: str):
        sg.popup_error(mensagem, title="[ERRO]", keep_on_top=True)

    def tela_opcoes(self):

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

        window = sg.Window('Menu Clínicas', layout, modal=True, element_justification='center')
        event, _ = window.read()
        window.close()
        
     
        return event if event is not None else 0

    def ler_dados_clinica(self):

        layout = [
            [sg.Text('--- Dados da Clínica ---', font=('Helvetica', 12, 'bold'))],
            [sg.Text('Nome da Clínica:', size=(15, 1)), sg.InputText(key='nome', size=(30, 1))],
            [sg.Text('Cidade:', size=(15, 1)), sg.InputText(key='cidade', size=(30, 1))],
            [sg.Text('Descrição:', size=(15, 1)), sg.InputText(key='descricao', size=(30, 1))],
            [sg.HSeparator(pad=(0, 10))],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Dados da Clínica', layout, modal=True)
        event, values = window.read()
        window.close()

        if event == 'Confirmar':
            return values['nome'].strip(), values['cidade'].strip(), values['descricao'].strip()
        
       
        return "", "", ""

    def mostrar_clinica(self, nome: str, cidade: str):
        sg.popup_ok(f"Clínica: {nome}\nCidade: {cidade}", title="Informações da Clínica", keep_on_top=True)

    def ler_dados_exclusao(self):
        layout = [
            [sg.Text('--- Buscar Clínica ---', font=('Helvetica', 12, 'bold'))],
            [sg.Text('Nome da Clínica:', size=(15, 1)), sg.InputText(key='nome', size=(30, 1))],
            [sg.Text('Cidade da Clínica:', size=(15, 1)), sg.InputText(key='cidade', size=(30, 1))],
            [sg.HSeparator(pad=(0, 10))],
            [sg.Button('Buscar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Buscar Clínica', layout, modal=True)
        event, values = window.read()
        window.close()

        if event == 'Buscar':
            return values['nome'].strip(), values['cidade'].strip()
        return "", ""

