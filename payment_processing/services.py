from .models import PaymentType, PaymentAction
from .commands import PaymentCommandFactory

class PaymentProcessingService:
    def process_payment(self, payment_type_name):
        try:
            payment_type = PaymentType.objects.get(name=payment_type_name)

            payment_actions = PaymentAction.objects.filter(tipo_pagamento=payment_type)

            for payment_action in payment_actions:
                self.execute_payment_action(payment_action)

            return "Payment processed with success."
        except PaymentType.DoesNotExist:
            return f"Payment type '{payment_type_name}' not found."


    def execute_payment_action(self, payment_action):
        command_class = PaymentCommandFactory.get_command_class(payment_action.descricao)
        command_instance = command_class()

        command_instance.execute()
