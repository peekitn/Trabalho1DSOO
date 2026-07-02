from views.tela_clinica import TelaClinica
from models.atendimento import Clinica, DadoObrigatorioException, RegistroDuplicadoException
from daos.clinica_dao import ClinicaDAO

class RegistroNaoEncontradoException(Exception):
    def __init__(self, mensagem="O registro solicitado não existe."):
        super().__init__(mensagem)

class ControladorClinica:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__view = TelaClinica()
        self.__clinica_dao = ClinicaDAO()

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

    # MÉTODO AUXILIAR PARA GERAR A CHAVE E BUSCAR NO DAO
    def buscar_clinica(self, nome: str, cidade: str):
        chave = f"{nome.lower()}_{cidade.lower()}"
        return self.__clinica_dao.get(chave)

    def cadastrar_clinica(self):
        try:
            nome, cidade, descricao = self.__view.ler_dados_clinica()

            if not nome or not cidade:
                raise DadoObrigatorioException("Nome e Cidade sao obrigatorios para cadastro de clinica.")

            # Busca direta no DAO usando a chave composta
            clinica_existente = self.buscar_clinica(nome, cidade)
            if clinica_existente:
                raise RegistroDuplicadoException("Ja existe uma clinica cadastrada com este nome nesta cidade.")

            nova_clinica = Clinica(nome, cidade, descricao)
            
            # Salva no arquivo
            self.__clinica_dao.add(nova_clinica)
            
            self.__view.mostrar_mensagem("Clinica cadastrada com sucesso!")
            return nova_clinica

        except (DadoObrigatorioException, RegistroDuplicadoException) as e:
            self.__view.mostrar_erro(str(e))
        except Exception as e:
            self.__view.mostrar_erro(f"Erro ao cadastrar clinica: {str(e)}")

    def listar_clinicas(self):
        clinicas = self.__clinica_dao.get_all()
        
        if not clinicas:
            self.__view.mostrar_mensagem("Nenhuma clinica cadastrada.")
            return

        self.__view.mostrar_mensagem("Lista de Clinicas:")
        for clinica in clinicas:
            self.__view.mostrar_clinica(clinica.nome, clinica.cidade)

    def excluir_clinica(self): 
        try:
            nome, cidade = self.__view.ler_dados_exclusao()

            if not nome or not cidade:
                raise DadoObrigatorioException("Nome e Cidade sao obrigatorios para realizar a exclusao.")

            clinica_para_remover = self.buscar_clinica(nome, cidade)

            if not clinica_para_remover:
                raise RegistroNaoEncontradoException("Clinica nao encontrada para exclusao.")
            
            # Remove usando a chave composta
            chave_remover = f"{nome.lower()}_{cidade.lower()}"
            self.__clinica_dao.remove(chave_remover)
            
            self.__view.mostrar_mensagem("Clinica excluida com sucesso!")

        except (DadoObrigatorioException, RegistroNaoEncontradoException) as e:
            self.__view.mostrar_erro(str(e))
        except Exception as e:
            self.__view.mostrar_erro(f"Erro ao excluir clinica: {str(e)}")

    def alterar_clinica(self):
        try:
            nome, cidade = self.__view.ler_dados_exclusao()

            if not nome or not cidade:
                raise DadoObrigatorioException("Nome e Cidade sao obrigatorios para buscar a clinica.")

            clinica_para_alterar = self.buscar_clinica(nome, cidade)

            if not clinica_para_alterar:
                raise RegistroNaoEncontradoException("Clinica nao encontrada para alteracao.")

            self.__view.mostrar_mensagem("Digite os NOVOS dados da clinica:")
            novo_nome, nova_cidade, nova_descricao = self.__view.ler_dados_clinica()

            if not novo_nome or not nova_cidade:
                raise DadoObrigatorioException("Novo Nome e Cidade sao obrigatorios.")

            chave_antiga = f"{nome.lower()}_{cidade.lower()}"
            chave_nova = f"{novo_nome.lower()}_{nova_cidade.lower()}"

            # BLINDAGEM: Se a chave mudar, checa se a nova já não existe
            if chave_antiga != chave_nova:
                clinica_conflito = self.buscar_clinica(novo_nome, nova_cidade)
                if clinica_conflito:
                    raise RegistroDuplicadoException("Ja existe outra clinica com este nome e cidade.")
                
                # Apaga o registro da chave velha no arquivo
                self.__clinica_dao.remove(chave_antiga)

            # Atualiza os dados no objeto
            clinica_para_alterar.nome = novo_nome
            clinica_para_alterar.cidade = nova_cidade
            clinica_para_alterar.descricao = nova_descricao

            # Salva no arquivo (cria a chave nova automaticamente pelo método add)
            self.__clinica_dao.add(clinica_para_alterar)

            self.__view.mostrar_mensagem("Clinica alterada com sucesso!")

        except (DadoObrigatorioException, RegistroNaoEncontradoException, RegistroDuplicadoException) as e:
            self.__view.mostrar_erro(str(e))
        except Exception as e:
            self.__view.mostrar_erro(f"Erro ao alterar clinica: {str(e)}")