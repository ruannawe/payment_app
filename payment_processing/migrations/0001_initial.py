# Generated by Django 4.2.7 on 2023-12-06 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('description', models.TextField()),
                ('owner_class', models.CharField(db_index=True, max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentTypeActionAssociation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_action', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payment_processing.paymentaction')),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payment_processing.paymenttype')),
            ],
            options={
                'unique_together': {('payment_type', 'payment_action')},
            },
        ),
        migrations.AddField(
            model_name='paymenttype',
            name='actions',
            field=models.ManyToManyField(through='payment_processing.PaymentTypeActionAssociation', to='payment_processing.paymentaction'),
        ),
    ]
