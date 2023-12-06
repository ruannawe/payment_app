from django.test import TestCase
from django.db import transaction, IntegrityError
from .models import PaymentAction, PaymentType, PaymentTypeActionAssociation

class PaymentModelsTest(TestCase):

    def setUp(self):
        self.action1 = PaymentAction.objects.create(
            name='Action 1',
            description='Description for Action 1',
            owner_class='OwnerClass1'
        )
        self.type1 = PaymentType.objects.create(name='Type 1')

    def test_payment_action_creation(self):
        self.assertEqual(self.action1.name, 'Action 1')
        self.assertEqual(self.action1.description, 'Description for Action 1')
        self.assertEqual(self.action1.owner_class, 'OwnerClass1')

    def test_payment_type_creation(self):
        self.assertEqual(self.type1.name, 'Type 1')

    def test_payment_type_action_association_creation(self):
        association = PaymentTypeActionAssociation.objects.create(
            payment_type=self.type1,
            payment_action=self.action1
        )
        self.assertEqual(str(association), 'Type 1 - Action 1')

    def test_unique_constraints(self):
        # Test unique constraints for PaymentAction
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                PaymentAction.objects.create(
                    name='Action 1',
                    description='Different Description',
                    owner_class='DifferentOwnerClass'
                )

        # Test unique constraints for PaymentType
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                PaymentType.objects.create(name='Type 1')

        # Create another PaymentAction
        action2 = PaymentAction.objects.create(
            name='Action 2',
            description='Description for Action 2',
            owner_class='OwnerClass2'
        )

        # Test unique_together constraint for PaymentTypeActionAssociation
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                PaymentTypeActionAssociation.objects.create(
                    payment_type=self.type1,
                    payment_action=action2
                )
                PaymentTypeActionAssociation.objects.create(
                    payment_type=self.type1,
                    payment_action=action2
                )