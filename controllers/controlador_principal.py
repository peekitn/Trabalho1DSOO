from controllers.controlador_relatorios import ControladorRelatorios
from controllers.controlador_paciente import ControladorPaciente
from controllers.controlador_atendimento import ControladorAtendimento
from controllers.controlador_clinica import ControladorClinica
from controllers.controlador_profissional import ControladorProfissional
from views.tela_principal import TelaPrincipal

class ControladorPrincipal:
    # guardar a instância única (Singleton)
    __instance = None

    def __init__(self):
        self.__view = TelaPrincipal()
        
        self.__controlador_paciente = ControladorPaciente(self)
        self.__controlador_clinica = ControladorClinica(self)
        self.__controlador_atendimento = ControladorAtendimento(self)
        self.__controlador_profissional = ControladorProfissional(self)
        self.__controlador_relatorios = ControladorRelatorios(self)

    #  Método para garantir o Singleton 
    def __new__(cls):
        if ControladorPrincipal.__instance is None:
            ControladorPrincipal.__instance = object.__new__(cls)
        return ControladorPrincipal.__instance

    def run(self):
        while True:
            try:
                opcao = self.__view.tela_opcoes()
                
                if opcao == 1:
                    self.__controlador_paciente.abrir_tela()
                elif opcao == 2:
                    self.__controlador_clinica.abrir_tela()
                elif opcao == 3:
                    self.__controlador_relatorios.abrir_tela()
                elif opcao == 4:
                    self.__controlador_atendimento.abrir_tela()
                elif opcao == 5:
                    self.__controlador_profissional.abrir_tela()
                elif opcao == 0:
                    self.__view.mostrar_mensagem("Encerrando o sistema...")
                    break
                else:
                    self.__view.mostrar_erro("Opcao invalida. Escolha um numero do menu.")
            
            except ValueError:
                self.__view.mostrar_erro("Entrada invalida! Por favor, digite um numero inteiro.")