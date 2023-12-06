from .models import PaymentType, PaymentTypeActionAssociation
from .commands import PaymentCommandFactory


class PaymentProcessingService:
    def process_payment(self, payment_type_name):
        try:
            payment_type = PaymentType.objects.get(name=payment_type_name)
            associations = PaymentTypeActionAssociation.objects.filter(payment_type=payment_type)
            payment_actions = [assoc.payment_action for assoc in associations]

            for payment_action in payment_actions:
                self.execute_payment_action(payment_action)

            return "Payment processed with success."
        except PaymentType.DoesNotExist:
            return f"Payment type '{payment_type_name}' not found."


    def execute_payment_action(self, payment_action):
        command_class = PaymentCommandFactory.get_command_class(payment_action.owner_class)
        command_instance = command_class()
        command_instance.execute()
