from django.shortcuts import render, get_object_or_404, redirect
from payment_processing.models import PaymentType, PaymentAction


def index(request):
    payment_types = PaymentType.objects.all()
    return render(request, 'index.html', {'payment_types': payment_types})


def edit(request, id):
    payment_type = get_object_or_404(PaymentType, id=id)
    payment_actions = payment_type.actions.all()
    all_actions = PaymentAction.objects.exclude(id__in=payment_actions.values_list('id', flat=True))

    return render(request, 'edit.html', {
        'payment_type': payment_type,
        'payment_actions': payment_actions,
        'all_actions': all_actions
    })


def update(request, id):
    payment_type = get_object_or_404(PaymentType, id=id)

    if request.method == 'POST':
        print(request.POST)
        if 'remove_action' in request.POST:
            action_id = request.POST.get('remove_action')
            payment_type.actions.remove(action_id)
        elif 'add_action' in request.POST:
            action_id = request.POST.get('new_action')
            payment_type.actions.add(action_id)

        return redirect('index')

    return redirect('edit', id=id)
