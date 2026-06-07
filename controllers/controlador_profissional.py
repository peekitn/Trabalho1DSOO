from views.tela_profissional import TelaProfissional
from models.pessoas import Profissional
from models.atendimento import DadoObrigatorioException, RegistroDuplicadoException

class CpfInvalidoException(Exception):
    def __init__(self, mensagem="CPF invalido. Deve conter 11 digitos numericos."):
        super().__init__(mensagem)

class ControladorProfissional:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__view = TelaProfissional()

    def abrir_tela(self):
        while True:
            try:
                opcao = self.__view.tela_opcoes()
                if opcao == 1:
                    self.cadastrar_profissional()
                elif opcao == 2:
                    self.listar_profissionais()
                elif opcao == 0:
                    break
                else:
                    self.__view.mostrar_erro("Opcao invalida.")
            except ValueError:
                self.__view.mostrar_erro("Digite um numero inteiro valido.")

    def _validar_cpf(self, cpf: str):
        if not cpf.isdigit() or len(cpf) != 11:
            raise CpfInvalidoException()

    def buscar_profissional_por_cpf(self, cpf: str):
        for prof in self.__controlador_principal.profissionais:
            if prof.cpf == cpf:
                return prof
        return None

    def cadastrar_profissional(self):
        try:
            nome, celular, cpf, especialidade, registro = self.__view.ler_dados_profissional()

            if not nome or not especialidade or not registro:
                raise DadoObrigatorioException("Nome, especialidade e registro sao obrigatorios.")
            
            self._validar_cpf(cpf)

            for prof in self.__controlador_principal.profissionais:
                if prof.cpf == cpf:
                    raise RegistroDuplicadoException(f"O CPF {cpf} ja esta cadastrado no sistema.")
                if prof.registro_profissional == registro:
                    raise RegistroDuplicadoException(f"O registro {registro} ja esta vinculado a outro profissional.")

            novo_profissional = Profissional(nome, celular, cpf, especialidade, registro)
            self.__controlador_principal.profissionais.append(novo_profissional)
            
            self.__view.mostrar_mensagem(f"Profissional {nome} cadastrado com sucesso!")
            return novo_profissional

        except (DadoObrigatorioException, CpfInvalidoException, RegistroDuplicadoException) as e:
            self.__view.mostrar_erro(str(e))
        except Exception as e:
            self.__view.mostrar_erro(f"Erro ao cadastrar profissional: {str(e)}")

    def listar_profissionais(self):
        if not self.__controlador_principal.profissionais:
            self.__view.mostrar_mensagem("Nenhum profissional cadastrado.")
            return

        self.__view.mostrar_mensagem("Lista de Profissionais:")
        for prof in self.__controlador_principal.profissionais:
            self.__view.mostrar_profissional(prof.nome, prof.cpf, prof.especialidade, prof.registro_profissional)

    def excluir_profissional(self):
        try:
            cpf = self.__view.ler_dado_exclusao()
            self._validar_cpf(cpf)

            profissional_para_remover = self.buscar_profissional_por_cpf(cpf)
            if not profissional_para_remover:
                raise RegistroNaoEncontradoException(f"Profissional com CPF {cpf} não encontrado.")
            self.__profissionais_cadastrados.remove(profissional_para_remover)
            self.__view.mostrar_mensagem("Profissional excluído com sucesso!")

        except (CpfInvalidoException, RegistroNaoEncontradoException) as e:
            self.__view.mostrar_erro(str(e))
        except Exception as e:
            self.__view.mostrar_erro(f"Erro ao excluir profissional: {str(e)}")
