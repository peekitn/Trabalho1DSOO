from views.tela_clinica import TelaClinica
from models.atendimento import Clinica, DadoObrigatorioException, RegistroDuplicadoException

class ControladorClinica:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__view = TelaClinica()

    def abrir_tela(self):
        while True:
            try:
                opcao = self.__view.tela_opcoes()
                if opcao == 1:
                    self.cadastrar_clinica()
                elif opcao == 2:
                    self.listar_clinicas()
                elif opcao == 0:
                    break
                else:
                    self.__view.mostrar_erro("Opcao invalida.")
            except ValueError:
                self.__view.mostrar_erro("Digite um numero inteiro valido.")

    def cadastrar_clinica(self):
        try:
            nome, cidade, descricao = self.__view.ler_dados_clinica()

            if not nome or not cidade:
                raise DadoObrigatorioException("Nome e Cidade sao obrigatorios para cadastro de clinica.")

            # Busca na lista central do Controlador Principal
            for clinica in self.__controlador_principal.clinicas:
                if clinica.nome.lower() == nome.lower() and clinica.cidade.lower() == cidade.lower():
                    raise RegistroDuplicadoException("Ja existe uma clinica cadastrada com este nome nesta cidade.")

            # Instancia e salva no banco central
            nova_clinica = Clinica(nome, cidade, descricao)
            self.__controlador_principal.clinicas.append(nova_clinica)
            
            self.__view.mostrar_mensagem("Clinica cadastrada com sucesso!")
            return nova_clinica

        except (DadoObrigatorioException, RegistroDuplicadoException) as e:
            self.__view.mostrar_erro(str(e))
        except Exception as e:
            self.__view.mostrar_erro(f"Erro ao cadastrar clinica: {str(e)}")

    def listar_clinicas(self):
        # Varre a lista central do Controlador Principal
        if not self.__controlador_principal.clinicas:
            self.__view.mostrar_mensagem("Nenhuma clinica cadastrada.")
            return

        self.__view.mostrar_mensagem("Lista de Clinicas:")
        for clinica in self.__controlador_principal.clinicas:
            # Envia os dados para a View renderizar
            self.__view.mostrar_clinica(clinica.nome, clinica.cidade)