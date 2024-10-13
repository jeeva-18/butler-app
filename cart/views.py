from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from products.models import Product
from .models import Cart, Cartitem
from django.http import JsonResponse

def cart_add(request,product_id):
    cart_id = request.session.get('cart_id')

    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            cart = Cart.objects.create()
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
    
    product = get_object_or_404(Product,id=product_id)

    cart_item, created = Cartitem.objects.get_or_create(cart=cart,product=product)

    if not created:
        cart_item.quantity += 1

    cart_item.save()

    response_data = {
        'success' : True,
        'message' : f"Added {product.name} to cart"
    }

    return JsonResponse(response_data)

def cart_detail(request):
    cart_id = request.session.get('cart_id')
    cart = None

    if cart_id:
        cart = get_object_or_404(Cart, id=cart_id)
    if not cart or not cart.items.exists():
        cart = None

    return render(request, "cart/detail.html", {"cart" : cart})


def cart_increment(request,product_id):
    cart_id = request.session.get('cart_id')
    cart = get_object_or_404(Cart,id=cart_id)
    item = get_object_or_404(Cartitem,id=product_id,cart=cart)
    item.quantity +=1 
    item.save()
    print(item.quantity)

    return redirect('cart:cart_detail')

def cart_decrement(request,product_id):
    cart_id = request.session.get('cart_id')
    cart = get_object_or_404(Cart,id=cart_id)
    item = get_object_or_404(Cartitem,id=product_id,cart=cart)
    item.quantity -=1
    if item.quantity == 0:
        item.delete()
    else:
        item.save()
    return redirect('cart:cart_detail')
