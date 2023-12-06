from django.test import TestCase, Client
from django.db import transaction, IntegrityError
from django.urls import reverse
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


class PaymentViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.payment_action1 = PaymentAction.objects.create(
            name='Action 1',
            description='Test Description 1',
            owner_class='TestClass1'
        )
        self.payment_type1 = PaymentType.objects.create(name='Type 1')
        self.payment_type1.actions.add(self.payment_action1)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn(self.payment_type1, response.context['payment_types'])

    def test_edit_view(self):
        response = self.client.get(reverse('edit', args=[self.payment_type1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit.html')
        self.assertEqual(response.context['payment_type'], self.payment_type1)
        self.assertIn(self.payment_action1, response.context['payment_actions'])

    def test_update_view_remove_action(self):
        response = self.client.post(reverse('update', args=[self.payment_type1.id]), {
            'remove_action': self.payment_action1.id
        })
        self.assertEqual(response.status_code, 302)
        self.payment_type1.refresh_from_db()
        self.assertNotIn(self.payment_action1, self.payment_type1.actions.all())

    def test_update_view_add_action(self):
        payment_action2 = PaymentAction.objects.create(
            name='Action 2',
            description='Test Description 2',
            owner_class='TestClass2'
        )

        self.payment_type1.actions.add(payment_action2)

        self.payment_type1.refresh_from_db()
        self.assertIn(payment_action2, self.payment_type1.actions.all())
