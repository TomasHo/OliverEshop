from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(objednavka=order,
                                         produkt=item['product'],
                                         cena=item['price'],
                                         mnozstvo=item['quantity'] )
            # clear the cart
            cart.clear()
            return render(request, 'orders/order/created.html',
                          {'objednavka': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})
