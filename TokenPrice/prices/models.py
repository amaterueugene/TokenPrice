from django.db import models

class Token(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    short_name = models.CharField(max_length=100, verbose_name='ShortName')
    price = models.FloatField(verbose_name='TokenPrice')
    change_day = models.FloatField(verbose_name='24hChange')
    volume_day = models.FloatField(verbose_name='24hVolume')
    market_cap = models.FloatField(verbose_name='MarketCap')
