from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Currency, ExchangeRate
from .serializers import CurrencySerializer, ExchangeRateSerializer


class CurrencyListView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class ExchangeRateView(APIView):
    def get(self, request, currency1, currency2):
        pair = f"{currency1}{currency2}"
        exchange_rate = ExchangeRate.objects.filter(currency_pair = pair).order_by("-retrieved_date").first()

        if exchange_rate:
            serializer = ExchangeRateSerializer(exchange_rate)
            return Response(serializer.data)
        return Response({"error": "exchange not found"}, status=404)