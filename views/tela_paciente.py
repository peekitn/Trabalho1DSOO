import FreeSimpleGUI as sg

class TelaPaciente:
    def __init__(self):
        sg.theme('LightBlue')

    def mostrar_mensagem(self, mensagem: str):
        sg.popup_ok(mensagem, title="[SISTEMA]", keep_on_top=True)

    def mostrar_erro(self, mensagem: str):
        sg.popup_error(mensagem, title="[ERRO]", keep_on_top=True)

    def tela_opcoes(self):

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

        window = sg.Window('Menu Pacientes', layout, modal=True, element_justification='center')
        event, _ = window.read()
        window.close()
        
        return event if event is not None else 0

    def pegar_dados_paciente(self):

        layout = [
            [sg.Text('--- Dados do Paciente ---', font=('Helvetica', 12, 'bold'))],
            [sg.Text('Nome:', size=(28, 1)), sg.InputText(key='nome', size=(25, 1))],
            [sg.Text('CPF:', size=(28, 1)), sg.InputText(key='cpf', size=(25, 1))],
            [sg.Text('Celular:', size=(28, 1)), sg.InputText(key='celular', size=(25, 1))],
            [sg.Text('Data de Nascimento (DD/MM/AAAA):', size=(28, 1)), sg.InputText(key='data_nascimento', size=(15, 1))],
            [sg.HSeparator(pad=(0, 10))],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Cadastrar/Alterar Paciente', layout, modal=True)
        event, values = window.read()
        window.close()

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
        sg.popup_ok(texto_exibicao, title="Dados do Paciente", keep_on_top=True)
