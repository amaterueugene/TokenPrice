from django.shortcuts import render
from django.views.generic import ListView
from .models import Token


class TokenPriceList(ListView):
    model = Token
    template_name = 'prices/token_price_list.html'
    context_object_name = 'tokens'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = ' - Prices'
        return context
    
