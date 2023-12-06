from django.db import migrations


def create_seed_data(apps, schema_editor):
    PaymentType = apps.get_model('payment_processing', 'PaymentType')
    PaymentAction = apps.get_model('payment_processing', 'PaymentAction')
    PaymentTypeActionAssociation = apps.get_model('payment_processing', 'PaymentTypeActionAssociation')

    payment_type_to_actions = {
        'Pagamento por Produto Físico': [
            {
                'name': 'Ação: Gerar uma guia de remessa para envio.',
                'description': 'Ação: Gerar uma guia de remessa para envio.',
                'owner_class': 'PaymentActionPackingSlipForShippingCommand',
            },
            {
                'name': 'Ação Adicional: Gerar pagamento de comissão ao agente.',
                'description': 'Ação Adicional: Gerar pagamento de comissão ao agente.',
                'owner_class': 'PaymentActionGenerateCommissionCommand',
            },
        ],
        'Pagamento por Livro': [
            {
                'name': 'Ação: Criar uma guia de remessa duplicada para o departamento de royalties.',
                'description': 'Ação: Criar uma guia de remessa duplicada para o departamento de royalties.',
                'owner_class': 'PaymentActionDuplicateShippingSlipForRoyaltiesCommand',
            },
            {
                'name': 'Ação Adicional: Gerar pagamento de comissão ao agente.',
                'description': 'Ação Adicional: Gerar pagamento de comissão ao agente.',
                'owner_class': 'PaymentActionGenerateCommissionForBookCommand',
            },
        ],
        'Pagamento por Nova Associação de Membro': [
            {
                'name': 'Ação: Ativar a associação de membro.',
                'description': 'Ação: Ativar a associação de membro.',
                'owner_class': 'PaymentActionActivateMembershipCommand',
            },
            {
                'name': 'Ação Adicional: Enviar um e-mail ao proprietário informando sobre a ativação.',
                'description': 'Ação Adicional: Enviar um e-mail ao proprietário informando sobre a ativação.',
                'owner_class': 'PaymentActionSendActivationEmailCommand',
            },
        ],
        'Pagamento por Upgrade de Associação': [
            {
                'name': 'Ação: Aplicar o upgrade na associação existente.',
                'description': 'Ação: Aplicar o upgrade na associação existente.',
                'owner_class': 'PaymentActionApplyUpgradeCommand',
            },
            {
                'name': 'Ação Adicional: Enviar um e-mail ao proprietário informando sobre o upgrade.',
                'description': 'Ação Adicional: Enviar um e-mail ao proprietário informando sobre o upgrade.',
                'owner_class': 'PaymentActionSendUpgradeEmailCommand',
            },
        ],
        'Pagamento por Vídeo "Aprendendo a Esquiar"': [
            {
                'name': 'Ação: Adicionar um vídeo gratuito "Primeiros Socorros" à guia de remessa (devido a uma decisão judicial de 1997).',
                'description': 'Ação: Adicionar um vídeo gratuito "Primeiros Socorros" à guia de remessa (devido a uma decisão judicial de 1997).',
                'owner_class': 'PaymentActionAddFreeVideoCommand',
            },
        ],
        # Add similar data for other payment types
    }

    for payment_type_name, action_details_list in payment_type_to_actions.items():
        payment_type, created = PaymentType.objects.get_or_create(name=payment_type_name)

        for action_details in action_details_list:
            payment_action, action_created = PaymentAction.objects.get_or_create(
                name=action_details['name'],
                defaults={'description': action_details['description'], 'owner_class': action_details['owner_class']}
            )

            PaymentTypeActionAssociation.objects.create(
                payment_type=payment_type,
                payment_action=payment_action
            )

class Migration(migrations.Migration):

    dependencies = [
        ('payment_processing', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_seed_data),
    ]
