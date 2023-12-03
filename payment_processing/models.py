from django.db import models


class PaymentType(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name


class PaymentAction(models.Model):
    type_payment = models.ForeignKey(PaymentType, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.TextField()
    owner_class = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
