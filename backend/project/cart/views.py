from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, F
from .models import CartItem
from project.products.models import Product

def _get_session_key(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def cart_detail(request):
    session_key = _get_session_key(request)
    qs = CartItem.objects.filter(session_key=session_key)
    total = qs.aggregate(total=Sum(F("product__price") * F("quantity")))["total"] or 0
    return render(request, "cart/detail.html", {"items": qs, "total": total})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    session_key = _get_session_key(request)
    item, created = CartItem.objects.get_or_create(
        session_key=session_key, product=product,
        defaults={"quantity": 1}
    )
    if not created:
        item.quantity += 1
        item.save()
    return redirect("cart_detail")

def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect("cart_detail")
