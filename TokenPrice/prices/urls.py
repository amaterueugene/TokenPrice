from django.urls import path
from .views import TokenPriceList
from .rest.views import TokenAPIView

urlpatterns = [
    path('', TokenPriceList.as_view(), name='PriceListPage'),
    #API
    path('api/v1/', TokenAPIView.as_view(), name='PriceListAPI'),
]
