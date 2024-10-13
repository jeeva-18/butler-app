from django.shortcuts import render,HttpResponse, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from orders.models import Order, OrderItem



def front(request):
    return render(request,'kitchen/front.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('kitchen:dashboard')
        else:
            messages.success(request,("Enter correct username or password"))
            return redirect('kitchen:login')
    else:
        return render(request,'kitchen/login.html')
    
def logout_user(request):
    logout(request)
    return redirect('kitchen:front')

@login_required(login_url='kitchen:login')
def dasboard_view(request):
    orders = Order.objects.all()
    return render(request,'kitchen/dashboard.html',{'orders':orders})


def dash_details(request,id):
    order = get_object_or_404(Order,id=id)
    return render(request, 'kitchen/details.html',{'id' : id,'order':order})


def remove_order(request,id):
    order = get_object_or_404(Order,id=id)
    order.delete()
    return redirect('kitchen:dashboard')

