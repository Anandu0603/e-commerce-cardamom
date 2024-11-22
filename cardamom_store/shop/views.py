from django.shortcuts import render, redirect
from .models import Cardamom, Order

def cardamom_list(request):
    cardamoms = Cardamom.objects.all()
    return render(request, 'shop/cardamom_list.html', {'cardamoms': cardamoms})

def place_order(request, cardamom_id):
    if request.method == "POST":
        cardamom = Cardamom.objects.get(id=cardamom_id)
        order = Order(
            cardamom=cardamom,
            buyer_name=request.POST['buyer_name'],
            buyer_address=request.POST['buyer_address'],
            quantity_ordered=request.POST['quantity_ordered']
        )
        order.save()
        return redirect('cardamom_list')
    
    return render(request, 'shop/place_order.html', {'cardamom_id': cardamom_id})