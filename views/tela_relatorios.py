import FreeSimpleGUI as sg

class TelaRelatorios:
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

    def tela_opcoes(self):

        layout = [
            [sg.Text('--- Menu de Relatórios ---', font=('Helvetica', 14, 'bold'), justification='center', expand_x=True)],
            [sg.HSeparator(pad=(0, 10))],
            
            [sg.Button('Clínicas com mais atendimentos', key=1, size=(35, 1))],
            [sg.Button('Atendimentos mais caros e mais baratos', key=2, size=(35, 1))],
            [sg.Button('Procedimentos mais realizados', key=3, size=(35, 1))],
            [sg.Button('Procedimentos mais caros e mais baratos', key=4, size=(35, 1))],
            
            [sg.HSeparator(pad=(0, 15))],
            [sg.Button('Retornar', key=0, button_color=('white', '#d32f2f'), size=(12, 1), expand_x=True)]
        ]

        window = sg.Window('Menu Relatórios', layout, modal=True, element_justification='center')
        event, _ = window.read()
        window.close()
        
        return event if event is not None else 0

    def mostrar_clinicas_mais_atendimentos(self, clinicas_ordenadas):
        if not clinicas_ordenadas:
            sg.popup_ok("Nenhum atendimento registrado no sistema.", title="Relatório de Clínicas", keep_on_top=True)
            return

        texto_relatorio = "--- Clínicas com Mais Atendimentos ---\n\n"
        for clinica, quantidade in clinicas_ordenadas:
            texto_relatorio += f"Clínica: {clinica} | Total de Atendimentos: {quantidade}\n"

        sg.popup_scrolled(texto_relatorio, title="Relatório de Clínicas", size=(50, 15), keep_on_top=True)

    def mostrar_atendimentos_extremos(self, mais_caro, mais_barato):
        if mais_caro and mais_barato:
            texto = (
                "--- Atendimentos Extremos ---\n\n"
                f"Mais Caro: Paciente {mais_caro.paciente.nome} - Valor: R$ {mais_caro.calcular_valor_total():.2f}\n"
                f"Mais Barato: Paciente {mais_barato.paciente.nome} - Valor: R$ {mais_barato.calcular_valor_total():.2f}"
            )
            sg.popup_ok(texto, title="Atendimentos Extremos", keep_on_top=True)
        else:
            sg.popup_ok("Nenhum atendimento registrado no sistema.", title="Atendimentos Extremos", keep_on_top=True)

    def mostrar_procedimentos_mais_realizados(self, procedimentos_ordenados):
        if not procedimentos_ordenados:
            sg.popup_ok("Nenhum procedimento registrado no sistema.", title="Procedimentos Mais Populares", keep_on_top=True)
            return

        texto_relatorio = "--- Procedimentos Mais Populares ---\n\n"
        for procedimento, quantidade in procedimentos_ordenados:
            texto_relatorio += f"Procedimento: {procedimento} | Realizados: {quantidade} vezes\n"

        sg.popup_scrolled(texto_relatorio, title="Procedimentos Mais Populares", size=(50, 15), keep_on_top=True)

    def mostrar_procedimentos_extremos(self, mais_caro, mais_barato):
        if mais_caro and mais_barato:
            texto = (
                "--- Procedimentos Extremos ---\n\n"
                f"Mais Caro: {mais_caro.descricao} - Custo: R$ {mais_caro.custo:.2f}\n"
                f"Mais Barato: {mais_barato.descricao} - Custo: R$ {mais_barato.custo:.2f}"
            )
            sg.popup_ok(texto, title="Procedimentos Extremos", keep_on_top=True)
        else:
            sg.popup_ok("Nenhum procedimento registrado no sistema.", title="Procedimentos Extremos", keep_on_top=True)

    def mostrar_mensagem(self, mensagem):
        sg.popup_ok(mensagem, title="[SISTEMA]", keep_on_top=True)
