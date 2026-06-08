# Francisco

from controllers.controlador_relatorios import ControladorRelatorios
from controllers.controlador_paciente import ControladorPaciente
from controllers.controlador_atendimento import ControladorAtendimento
from controllers.controlador_clinica import ControladorClinica
from controllers.controlador_profissional import ControladorProfissional
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
        
        # Instancia os controladores
        self.controlador_relatorios = ControladorRelatorios(self)
        self.controlador_paciente = ControladorPaciente(self)
        self.controlador_atendimento = ControladorAtendimento(self)
        self.controlador_clinica = ControladorClinica(self)
        self.controlador_profissional = ControladorProfissional(self)

    def iniciar(self):
        while True:
            try:
                opcao = self.tela_principal.tela_opcoes()
                
                if opcao == 1:
                    self.controlador_paciente.abrir_tela()
                elif opcao == 2:
                    self.controlador_clinica.abrir_tela()
                elif opcao == 3:
                    self.controlador_relatorios.abrir_tela()
                elif opcao == 4:
                    self.controlador_atendimento.abrir_tela()
                elif opcao == 5:
                    self.controlador_profissional.abrir_tela()
                elif opcao == 0:
                    self.tela_principal.mostrar_mensagem("Encerrando o sistema...")
                    break
                else:
                    self.tela_principal.mostrar_erro("Opcao invalida. Escolha um numero do menu.")
            
            except ValueError:
                self.tela_principal.mostrar_erro("Entrada invalida! Por favor, digite um numero inteiro.")