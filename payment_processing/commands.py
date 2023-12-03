class PaymentCommandFactory:
    @staticmethod
    def get_command_class(action_description):
        command_mapping = {
            "PagamentoProdutoFisico": PagamentoProdutoFisicoCommand,
            "PagamentoLivro": PagamentoLivroCommand,
        }

        return command_mapping.get(action_description, DefaultPaymentCommand)


class PagamentoProdutoFisicoCommand:
    def execute(self):
        pass


class PagamentoLivroCommand:
    def execute(self):
        pass


class DefaultPaymentCommand:
    def execute(self):
        print("Ação padrão para pagamento.")
