from views.tela_paciente import TelaPaciente
from models.pessoas import Paciente
from datetime import datetime
from daos.paciente_dao import PacienteDAO

class ControladorPaciente:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__view = TelaPaciente()
        self.__paciente_dao = PacienteDAO()

    def abrir_tela(self):
        while True:
            try:
                opcao = self.__view.tela_opcoes()
                if opcao == 1:
                    self.cadastrar_paciente()
                elif opcao == 2:
                    self.listar_pacientes()
                elif opcao == 3:
                    self.alterar_paciente()
                elif opcao == 4:
                    self.excluir_paciente()
                elif opcao == 0:
                    break
                else:
                    self.__view.mostrar_erro("Opcao invalida.")
            except ValueError:
                self.__view.mostrar_erro("Digite um numero inteiro valido.")

    def buscar_paciente_por_cpf(self, cpf):
        return self.__paciente_dao.get(cpf)

    def cadastrar_paciente(self):
        dados = self.__view.pegar_dados_paciente()
        paciente_existente = self.buscar_paciente_por_cpf(dados["cpf"])
        
        if paciente_existente:
            self.__view.mostrar_erro("Ja existe um paciente com este CPF.")
            return

        try:
            data_nasc_formatada = datetime.strptime(dados["data_nascimento"], "%d/%m/%Y").date()
            
            novo_paciente = Paciente(
                nome=dados["nome"], 
                celular=dados["celular"], 
                cpf=dados["cpf"], 
                data_nascimento=data_nasc_formatada
            )
            
            # AQUI FOI SUBSTITUIDO O .append() DA LISTA PELO .add() DO DAO
            self.__paciente_dao.add(novo_paciente)
            self.__view.mostrar_mensagem("Paciente cadastrado com sucesso!")
        except ValueError:
            self.__view.mostrar_erro("Formato de data invalido.")

    def listar_pacientes(self):
        # AQUI PEGA TODOS OS PACIENTES DO ARQUIVO .pkl
        pacientes = self.__paciente_dao.get_all()
        
        if len(pacientes) == 0:
            self.__view.mostrar_mensagem("Nenhum paciente cadastrado.")
            return
        
        self.__view.mostrar_mensagem("Lista de Pacientes:")
        for paciente in pacientes:
            dados = {
                "nome": paciente.nome, 
                "cpf": paciente.cpf, 
                "celular": paciente.celular,
                "data_nascimento": paciente.data_nascimento.strftime("%d/%m/%Y")
            }
            self.__view.mostrar_paciente(dados)

    def excluir_paciente(self):
        cpf = self.__view.selecionar_paciente()
        paciente = self.buscar_paciente_por_cpf(cpf)

        if not paciente:
            self.__view.mostrar_erro("Paciente nao encontrado.")
            return

        # AQUI SUBSTITUI O .remove() DA LISTA PELO .remove() DO DAO
        self.__paciente_dao.remove(paciente.cpf)
        self.__view.mostrar_mensagem("Paciente excluido com sucesso!")