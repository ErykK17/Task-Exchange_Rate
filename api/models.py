from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.code


class ExchangeRate(models.Model):
    currency_pair = models.CharField(max_length=10)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=6)
    retrieved_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.currency_pair}: {self.exchange_rate} {self.retrieved_date}"