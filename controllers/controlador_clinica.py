from views.tela_clinica import TelaClinica
from models.atendimento import Clinica, DadoObrigatorioException, RegistroDuplicadoException

        
class RegistroNaoEncontradoException(Exception):
    def __init__(self, mensagem="O registro solicitado não existe."):
        super().__init__(mensagem)

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
                elif opcao == 3:
                    self.excluir_clinica()
                elif opcao == 4:
                    self.alterar_clinica()
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

    def excluir_clinica(self): 
        try:
            nome, cidade = self.__view.ler_dados_exclusao()

            if not nome or not cidade:
                raise DadoObrigatorioException("Nome e Cidade sao obrigatorios para realizar a exclusao.")

            clinica_para_remover = None
            
            for clinica in self.__controlador_principal.clinicas:
                if clinica.nome.lower() == nome.lower() and clinica.cidade.lower() == cidade.lower():
                    clinica_para_remover = clinica
                    break

            if not clinica_para_remover:
                raise RegistroNaoEncontradoException("Clinica nao encontrada para exclusao.")
            
            self.__controlador_principal.clinicas.remove(clinica_para_remover)
            self.__view.mostrar_mensagem("Clinica excluida com sucesso!")

        except (DadoObrigatorioException, RegistroNaoEncontradoException) as e:
            self.__view.mostrar_erro(str(e))
        except Exception as e:
            self.__view.mostrar_erro(f"Erro ao excluir clinica: {str(e)}")

    def alterar_clinica(self):
        try:
            # Reaproveita a função de pedir o nome e cidade para achar a clínica
            nome, cidade = self.__view.ler_dados_exclusao()

            if not nome or not cidade:
                raise DadoObrigatorioException("Nome e Cidade sao obrigatorios para buscar a clinica.")

            clinica_para_alterar = None
            
            for clinica in self.__controlador_principal.clinicas:
                if clinica.nome.lower() == nome.lower() and clinica.cidade.lower() == cidade.lower():
                    clinica_para_alterar = clinica
                    break

            if not clinica_para_alterar:
                raise RegistroNaoEncontradoException("Clinica nao encontrada para alteracao.")

            self.__view.mostrar_mensagem("Digite os NOVOS dados da clinica:")
            novo_nome, nova_cidade, nova_descricao = self.__view.ler_dados_clinica()

            if not novo_nome or not nova_cidade:
                raise DadoObrigatorioException("Novo Nome e Cidade sao obrigatorios.")

            # Verifica se os novos dados já não existem em OUTRA clínica
            for clinica in self.__controlador_principal.clinicas:
                if clinica != clinica_para_alterar and clinica.nome.lower() == novo_nome.lower() and clinica.cidade.lower() == nova_cidade.lower():
                    raise RegistroDuplicadoException("Ja existe outra clinica com este nome e cidade.")

            # Atualiza os dados
            clinica_para_alterar.nome = novo_nome
            clinica_para_alterar.cidade = nova_cidade
            clinica_para_alterar.descricao = nova_descricao

            self.__view.mostrar_mensagem("Clinica alterada com sucesso!")

        except (DadoObrigatorioException, RegistroNaoEncontradoException, RegistroDuplicadoException) as e:
            self.__view.mostrar_erro(str(e))
        except Exception as e:
            self.__view.mostrar_erro(f"Erro ao alterar clinica: {str(e)}")
