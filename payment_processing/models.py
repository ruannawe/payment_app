from django.db import models


class PaymentAction(models.Model):
    name = models.CharField(max_length=300, unique=True, db_index=True)
    description = models.TextField()
    owner_class = models.CharField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name


class PaymentType(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    actions = models.ManyToManyField('PaymentAction', through='PaymentTypeActionAssociation')

    def __str__(self):
        return self.name


class PaymentTypeActionAssociation(models.Model):
    payment_type = models.ForeignKey(PaymentType, on_delete=models.PROTECT)
    payment_action = models.ForeignKey(PaymentAction, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.payment_type} - {self.payment_action}"

    class Meta:
        unique_together = ('payment_type', 'payment_action',)
