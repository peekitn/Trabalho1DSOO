class ControladorClinica:
    def __init__(self, view: TelaClinica):
        self.__view = view
        self.__clinicas_cadastradas = []

    def cadastrar_clinica(self):
        try:
            nome, cidade, descricao = self.__view.ler_dados_clinica()

            # Validação da regra de negócio
            if not nome or not cidade:
                raise DadoObrigatorioException("Nome e Cidade são obrigatórios para cadastro de clínica.")

            # Verifica se uma clínica já não foi cadastrada, para evitar o cadastro repetido.
            for clinica in self.__clinicas_cadastradas:
                if clinica.nome.lower() == nome.lower() and clinica.cidade.lower() == cidade.lower():
                    raise RegistroDuplicadoException("Já existe uma clínica cadastrada com este nome nesta cidade.")

            nova_clinica = Clinica(nome, cidade, descricao)
            self.__clinicas_cadastradas.append(nova_clinica)
            
            self.__view.mostrar_mensagem("Clínica cadastrada com sucesso!")
            return nova_clinica

        except (DadoObrigatorioException, RegistroDuplicadoException) as e:
            self.__view.mostrar_erro(str(e))
        except Exception as e:
            self.__view.mostrar_erro(f"Erro ao cadastrar clínica: {str(e)}")

    def listar_clinicas(self):
        if not self.__clinicas_cadastradas:
            self.__view.mostrar_mensagem("Nenhuma clínica cadastrada.")
            return

        self.__view.mostrar_mensagem("Lista de Clínicas")
        for clinica in self.__clinicas_cadastradas:
            print(f"- {clinica.nome} ({clinica.cidade})")