from views.tela_profissional import TelaProfissional
from models.pessoas import Profissional
from models.atendimento import DadoObrigatorioException, RegistroDuplicadoException
from daos.profissional_dao import ProfissionalDAO

class CpfInvalidoException(Exception):
    def __init__(self, mensagem="CPF invalido. Deve conter 11 digitos numericos."):
        super().__init__(mensagem)

class RegistroNaoEncontradoException(Exception):
    def __init__(self, mensagem="O registro solicitado não existe."):
        super().__init__(mensagem)

class ControladorProfissional:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__view = TelaProfissional()
        self.__profissional_dao = ProfissionalDAO()

    def abrir_tela(self):
        while True:
            try:
                opcao = self.__view.tela_opcoes()
                if opcao == 1:
                    self.cadastrar_profissional()
                elif opcao == 2:
                    self.listar_profissionais()
                elif opcao == 3:
                    self.excluir_profissional()
                elif opcao == 4:
                    self.alterar_profissional()
                elif opcao == 0:
                    break
                else:
                    self.__view.mostrar_erro("Opcao invalida.")
            except ValueError:
                self.__view.mostrar_erro("Digite um numero inteiro valido.")

    def _validar_cpf(self, cpf: str):
        if not cpf.isdigit() or len(cpf) != 11:
            raise CpfInvalidoException()

    # BUSCA SIMPLIFICADA COM DAO
    def buscar_profissional_por_cpf(self, cpf: str):
        return self.__profissional_dao.get(cpf)

    def cadastrar_profissional(self):
        try:
            nome, celular, cpf, especialidade, registro = self.__view.ler_dados_profissional()

            if not nome or not especialidade or not registro:
                raise DadoObrigatorioException("Nome, especialidade e registro sao obrigatorios.")
            
            self._validar_cpf(cpf)

            # VALIDAÇÃO DE DUPLICIDADE USANDO get_all()
            for prof in self.__profissional_dao.get_all():
                if prof.cpf == cpf:
                    raise RegistroDuplicadoException(f"O CPF {cpf} ja esta cadastrado no sistema.")
                if prof.registro_profissional == registro:
                    raise RegistroDuplicadoException(f"O registro {registro} ja esta vinculado a outro profissional.")

            novo_profissional = Profissional(nome, celular, cpf, especialidade, registro)
            
            # SALVA NO ARQUIVO
            self.__profissional_dao.add(novo_profissional)
            
            self.__view.mostrar_mensagem(f"Profissional {nome} cadastrado com sucesso!")
            return novo_profissional

        except (DadoObrigatorioException, CpfInvalidoException, RegistroDuplicadoException) as e:
            self.__view.mostrar_erro(str(e))
        except Exception as e:
            self.__view.mostrar_erro(f"Erro ao cadastrar profissional: {str(e)}")

    def listar_profissionais(self):
        profissionais = self.__profissional_dao.get_all()
        
        if not profissionais:
            self.__view.mostrar_mensagem("Nenhum profissional cadastrado.")
            return

        self.__view.mostrar_mensagem("Lista de Profissionais:")
        for prof in profissionais:
            self.__view.mostrar_profissional(prof.nome, prof.cpf, prof.especialidade, prof.registro_profissional)

    def excluir_profissional(self):
        try:
            cpf = self.__view.ler_dado_exclusao()
            self._validar_cpf(cpf)

            profissional_para_remover = self.buscar_profissional_por_cpf(cpf)
            if not profissional_para_remover:
                raise RegistroNaoEncontradoException(f"Profissional com CPF {cpf} nao encontrado.")
            
            # REMOVE DO ARQUIVO
            self.__profissional_dao.remove(cpf)
            self.__view.mostrar_mensagem("Profissional excluido com sucesso!")

        except (CpfInvalidoException, RegistroNaoEncontradoException) as e:
            self.__view.mostrar_erro(str(e))
        except Exception as e:
            self.__view.mostrar_erro(f"Erro ao excluir profissional: {str(e)}")

    def alterar_profissional(self):
        try:
            cpf = self.__view.ler_dado_exclusao()
            self._validar_cpf(cpf)

            profissional_para_alterar = self.buscar_profissional_por_cpf(cpf)
            if not profissional_para_alterar:
                raise RegistroNaoEncontradoException(f"Profissional com CPF {cpf} nao encontrado.")

            self.__view.mostrar_mensagem("Digite os NOVOS dados do profissional:")
            novo_nome, novo_celular, novo_cpf, nova_especialidade, novo_registro = self.__view.ler_dados_profissional()

            if not novo_nome or not nova_especialidade or not novo_registro:
                raise DadoObrigatorioException("Nome, especialidade e registro sao obrigatorios.")

            self._validar_cpf(novo_cpf)

            for prof in self.__profissional_dao.get_all():
                # Compara os CPFs para não bater com o próprio profissional sendo alterado
                if prof.cpf != cpf:
                    if prof.cpf == novo_cpf:
                        raise RegistroDuplicadoException(f"O CPF {novo_cpf} ja esta cadastrado.")
                    if prof.registro_profissional == novo_registro:
                        raise RegistroDuplicadoException(f"O registro {novo_registro} ja esta vinculado a outro profissional.")

            # SE O CPF MUDOU, PRECISAMOS APAGAR A CHAVE VELHA DO ARQUIVO
            if cpf != novo_cpf:
                self.__profissional_dao.remove(cpf)

            # Atualiza os dados
            profissional_para_alterar.nome = novo_nome
            profissional_para_alterar.celular = novo_celular
            profissional_para_alterar.cpf = novo_cpf
            profissional_para_alterar.especialidade = nova_especialidade
            profissional_para_alterar.registro_profissional = novo_registro

            # SALVA O OBJETO ATUALIZADO (se o CPF mudou, ele cria a chave nova automaticamente)
            self.__profissional_dao.add(profissional_para_alterar)

            self.__view.mostrar_mensagem("Profissional alterado com sucesso!")

        except (DadoObrigatorioException, CpfInvalidoException, RegistroNaoEncontradoException, RegistroDuplicadoException) as e:
            self.__view.mostrar_erro(str(e))
        except Exception as e:
            self.__view.mostrar_erro(f"Erro ao alterar profissional: {str(e)}")