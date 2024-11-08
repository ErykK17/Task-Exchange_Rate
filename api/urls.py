from django.urls import path

from .views import CurrencyListView, ExchangeRateView

urlpatterns = [
    path('currency/', CurrencyListView.as_view(), name='currency-list'),
    path('currency/<str:currency1>/<str:currency2>/', ExchangeRateView.as_view(), name='exchange-rate-detail'),
]