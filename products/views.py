from django.shortcuts import render, get_object_or_404

from .models import Category, Product

# Create your views here.

def product_list(request,table_no=None,category_slug=None):
    if table_no:
        request.session['table_no'] = table_no
    else:
        table_no = request.session['table_no']
    category = None
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)
    
    return render(request, 'products/product/list.html',{
        'table_no' : table_no,
        'category' : category,
        'products' : products,
        'categories' : categories,
    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    return render(request, 'products/product/details.html',{'product':product})