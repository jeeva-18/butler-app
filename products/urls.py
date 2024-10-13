from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('<int:table_no>/', views.product_list, name='product_list'),
    path('<int:table_no>/<slug:category_slug>/',views.product_list, name='product_list_by_category'),
    path('product/<int:id>/<slug:slug>/',views.product_detail, name='product_details'),
]