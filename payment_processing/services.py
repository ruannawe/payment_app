from .models import PaymentType, PaymentAction
from .commands import PaymentCommandFactory

class PaymentProcessingService:
    def process_payment(self, payment_type_name):
        try:
            # Buscar o tipo de pagamento pelo nome
            payment_type = PaymentType.objects.get(nome=payment_type_name)

            # Buscar as ações associadas ao tipo de pagamento
            payment_actions = PaymentAction.objects.filter(tipo_pagamento=payment_type)

            # Executar as ações associadas
            for payment_action in payment_actions:
                self.execute_payment_action(payment_action)

            return "Pagamento processado com sucesso."
        except PaymentType.DoesNotExist:
            return f"Tipo de pagamento '{payment_type_name}' não encontrado."

    def execute_payment_action(self, payment_action):
        # Obter a classe associada à ação e criar uma instância
        command_class = PaymentCommandFactory.get_command_class(payment_action.descricao)
        command_instance = command_class()

        # Executar o comando
        command_instance.execute()