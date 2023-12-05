from django.shortcuts import render
from payment_processing.models import PaymentType


def index(request):
    payment_types = PaymentType.objects.all()
    return render(request, 'index.html', {'payment_types': payment_types})
