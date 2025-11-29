from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Sum, F
from project.cart.models import CartItem
from .models import Order, OrderItem

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "orders/list.html", {"orders": orders})

@login_required
@transaction.atomic
def checkout(request):
    session_key = request.session.session_key
    cart_items = CartItem.objects.filter(session_key=session_key)
    if not cart_items.exists():
        return redirect("cart_detail")

    total = cart_items.aggregate(total=Sum(F("product__price") * F("quantity")))["total"] or 0
    order = Order.objects.create(user=request.user, total_amount=total)

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price,
        )
    cart_items.delete()
    # TODO: redirect to payments
    return render(request, "orders/confirm.html", {"order": order})
