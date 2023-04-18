from django.shortcuts import render
from django.views.generic import ListView
from .models import Token
from .token_parser import parse_tokens


class TokenPriceList(ListView):
    model = Token
    template_name = 'prices/price_list.html'
    context_object_name = 'tokens'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = ' - Prices'
        '''Updating tokens data in db when reloading the page'''
        Token.objects.all().delete()
        tokens_data = parse_tokens()
        for token in tokens_data:
            Token.objects.create(
                name=token[1], 
                short_name=token[2], 
                price=token[3],
                change_day=token[4],
                volume_day=token[5],
                volume_day_char=token[6],
                market_cap=token[7],
                market_cap_char=token[8])
        return context
    
