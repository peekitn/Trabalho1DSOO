from controllers.controlador_relatorios import ControladorRelatorios

class ControladorPrincipal:
    def __init__(self):
        self.clinicas = []
        self.pacientes = []
        self.profissionais = []
        self.atendimentos = []
        
        self.controlador_relatorios = ControladorRelatorios(self)

    def iniciar(self):
        pass