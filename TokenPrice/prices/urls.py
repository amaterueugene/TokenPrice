from django.urls import path, include
from .views import TokenPriceList

urlpatterns = [
    path('', TokenPriceList.as_view(), name='PriceListPage')
]
