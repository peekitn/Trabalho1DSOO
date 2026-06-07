class ControladorProfissional:
    def __init__(self, view: TelaProfissional):
        self.__view = view
        self.__profissionais_cadastrados = []

    def _validar_cpf(self, cpf: str):
        if not cpf.isdigit() or len(cpf) != 11:
            raise CpfInvalidoException()

    def cadastrar_profissional(self):
        try:
            nome, celular, cpf, especialidade, registro = self.__view.ler_dados_profissional()

            # Validações
            if not nome or not especialidade or not registro:
                raise DadoObrigatorioException("Nome, especialidade e registro profissional são obrigatórios.")
            
            self._validar_cpf(cpf)

            # Verifica se o CPF ou Registro Profissional já estão cadastrados, para evitar cadastro repetido.
            for prof in self.__profissionais_cadastrados:
                if prof.cpf == cpf:
                    raise RegistroDuplicadoException(f"O CPF {cpf} já está cadastrado no sistema.")
                if prof.registro_profissional == registro:
                    raise RegistroDuplicadoException(f"O registro {registro} já está vinculado a outro profissional.")

            novo_profissional = Profissional(nome, celular, cpf, especialidade, registro)
            self.__profissionais_cadastrados.append(novo_profissional)
            
            self.__view.mostrar_mensagem(f"Profissional {nome} cadastrado com sucesso!")
            return novo_profissional

        except (DadoObrigatorioException, CpfInvalidoException, RegistroDuplicadoException) as e:
            self.__view.mostrar_erro(str(e))
        except Exception as e:
            self.__view.mostrar_erro(f"Erro ao cadastrar profissional: {str(e)}")

    def buscar_profissional_por_cpf(self, cpf: str):
        for prof in self.__profissionais_cadastrados:
            if prof.cpf == cpf:
                return prof
        return None