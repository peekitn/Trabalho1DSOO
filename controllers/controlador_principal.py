from controllers.controlador_relatorios import ControladorRelatorios
from views.tela_principal import TelaPrincipal

class ControladorPrincipal:
    def __init__(self):
        # Banco de dados em memória
        self.clinicas = []
        self.pacientes = []
        self.profissionais = []
        self.atendimentos = []
        
        # Instancia a tela do menu inicial
        self.tela_principal = TelaPrincipal()
        
        # Instancia os controladores (os da dupla vão entrar aqui depois)
        self.controlador_relatorios = ControladorRelatorios(self)
        # self.controlador_paciente = ControladorPaciente(self)

    def iniciar(self):
        while True:
            opcao = self.tela_principal.tela_opcoes()
            
            if opcao == 1:
                # self.controlador_paciente.abrir_tela()
                print("Módulo em construção pela dupla...")
            elif opcao == 2:
                # self.controlador_clinica.abrir_tela()
                print("Módulo em construção pela dupla...")
            elif opcao == 3:
                self.controlador_relatorios.abrir_tela()
            elif opcao == 0:
                print("Sistema encerrado.")
                break
            else:
                print("Opção inválida.")