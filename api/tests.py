from django.test import TestCase
from rest_framework.test import APIClient

from .models import Currency, ExchangeRate


class CurrencyExchangeTests(TestCase):
    def setUp(self):
        Currency.objects.create(code="USD")
        Currency.objects.create(code="EUR")
        ExchangeRate.objects.create(currency_pair="EURUSD", exchange_rate="1.078167")

    def test_get_currency_list(self):
        client = APIClient()
        response = client.get('/api/currency/')
        self.assertEqual(response.status_code, 200)

    def test_get_exchange_rate(self):
        client = APIClient()
        response = client.get('/api/currency/EUR/USD/')
        self.assertEqual(response.status_code, 200)
