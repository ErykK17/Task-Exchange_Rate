import yfinance as yf
from django.core.management.base import BaseCommand

from api.models import Currency, ExchangeRate


class Command(BaseCommand):
    help = "Exctract currency pairs from yahoo finance databas."

    def handle(self, *args, **kwargs):
        
        currency_pairs = ["EURUSD=X", "USDJPY=X", "PLNUSD=X"]

        for pair in currency_pairs:
            data = yf.Ticker(pair)
            price = data.history(period="1d").iloc[-1]["Close"]

            currency1, currency2 = pair[:3], pair[3:6]
            first_currency_obj, _ = Currency.objects.get_or_create(code=currency1)
            second_currency_obj, _ = Currency.objects.get_or_create(code=currency2)

            ExchangeRate.objects.create(currency_pair=pair[:6], exchange_rate=price)
            self.stdout.write(self.style.SUCCESS(f'Successfully loaded {pair[:6]} rate: {price}'))