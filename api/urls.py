from django.urls import path, include
from rest_framework.authtoken import views
from .views import home

urlpatterns = [
    path('', home, name='api.home'),
    path('Category/',include('api.category.urls')),
    path('Product/',include('api.product.urls')),
    path('User/',include('api.user.urls')),
    path('Order/',include('api.order.urls')),
    path('Payment/',include('api.payment.urls')),
    path('api-token-auth/',views.obtain_auth_token,name='api-token-auth')
]
