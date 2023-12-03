# Generated by Django 4.2.7 on 2023-12-03 20:31

from django.db import migrations


def create_seed_data(apps, schema_editor):
    payment_type = apps.get_model('payment_processing', 'PaymentType')
    payment_action = apps.get_model('payment_processing', 'PaymentAction')

    # Create PaymentType instances
    payment_type.objects.create(name='Pagamento por Produto Físico')
    payment_type.objects.create(name='Pagamento por Livro')
    payment_type.objects.create(name='Pagamento por Nova Associação de Membro')
    payment_type.objects.create(name='Pagamento por Upgrade de Associação')
    payment_type.objects.create(name='Pagamento por Vídeo "Aprendendo a Esquiar"')

    # Create PaymentAction instances
    payment_action.objects.create(
        type_payment=payment_type.objects.get(name='Pagamento por Produto Físico'),
        name='Ação: Gerar uma guia de remessa para envio.',
        description='Ação: Gerar uma guia de remessa para envio.',
        owner_class='Owner 1'
    )

    payment_action.objects.create(
        type_payment=payment_type.objects.get(name='Pagamento por Produto Físico'),
        name='Ação Adicional: Gerar pagamento de comissão ao agente.',
        description='Ação Adicional: Gerar pagamento de comissão ao agente.',
        owner_class='Owner 1'
    )

    payment_action.objects.create(
        type_payment=payment_type.objects.get(name='Pagamento por Livro'),
        name='Ação: Criar uma guia de remessa duplicada para o departamento de royalties.',
        description='Ação: Criar uma guia de remessa duplicada para o departamento de royalties.',
        owner_class='Owner 2'
    )

    payment_action.objects.create(
        type_payment=payment_type.objects.get(name='Pagamento por Livro'),
        name='Ação Adicional: Gerar pagamento de comissão ao agente.',
        description='Ação Adicional: Gerar pagamento de comissão ao agente.',
        owner_class='Owner 2'
    )

    payment_action.objects.create(
        type_payment=payment_type.objects.get(name='Pagamento por Nova Associação de Membro'),
        name='Ação: Ativar a associação de membro.',
        description='Ação: Ativar a associação de membro.',
        owner_class='Owner 2'
    )

    payment_action.objects.create(
        type_payment=payment_type.objects.get(name='Pagamento por Nova Associação de Membro'),
        name='Ação Adicional: Enviar um e-mail ao proprietário informando sobre a ativação.',
        description='Ação Adicional: Enviar um e-mail ao proprietário informando sobre a ativação.',
        owner_class='Owner 2'
    )

    payment_action.objects.create(
        type_payment=payment_type.objects.get(name='Pagamento por Upgrade de Associação'),
        name='Ação: Aplicar o upgrade na associação existente.',
        description='Ação: Aplicar o upgrade na associação existente.',
        owner_class='Owner 2'
    )

    payment_action.objects.create(
        type_payment=payment_type.objects.get(name='Pagamento por Upgrade de Associação'),
        name='Ação Adicional: Enviar um e-mail ao proprietário informando sobre o upgrade.',
        description='Ação Adicional: Enviar um e-mail ao proprietário informando sobre o upgrade.',
        owner_class='Owner 2'
    )

    payment_action.objects.create(
        type_payment=payment_type.objects.get(name='Pagamento por Upgrade de Associação'),
        name='Ação Adicional: Enviar um e-mail ao proprietário informando sobre o upgrade.',
        description='Ação Adicional: Enviar um e-mail ao proprietário informando sobre o upgrade.',
        owner_class='Owner 2'
    )

    payment_action.objects.create(
        type_payment=payment_type.objects.get(name='Pagamento por Vídeo "Aprendendo a Esquiar"'),
        name='Ação: Adicionar um vídeo gratuito "Primeiros Socorros" à guia de remessa (devido a uma decisão judicial de 1997).',
        description='Ação: Adicionar um vídeo gratuito "Primeiros Socorros" à guia de remessa (devido a uma decisão judicial de 1997).',
        owner_class='Owner 2'
    )


class Migration(migrations.Migration):

    dependencies = [
        ('payment_processing', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_seed_data),
    ]
