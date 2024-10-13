from django.urls import path
from . import views

app_name = 'kitchen'

urlpatterns = [
    path('', views.front, name='front'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('dashboard/',views.dasboard_view,name='dashboard'),
    path('order/<int:id>/',views.dash_details,name='order_detail'),
    path('remove/<int:id>/',views.remove_order,name='remove_order'),
]