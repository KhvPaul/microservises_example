from django.shortcuts import render

# Create your views here.


from .tasks import sync_orders


def view(request):
    ...
    order = Order.objects.create(...)

    sync_orders.apply_async(args=(order.pk))