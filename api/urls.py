from django.urls import path

from api.views import ContractBalanceView, ownermintView, getNFTView_s, getNFTView_b

app_name = 'api'
urlpatterns = [
    path('getbalance/', ContractBalanceView.as_view(), name='get_balance'),
    path('ownermint/', ownermintView.as_view(), name='ownermint'),
    path('nft_s/', getNFTView_s.as_view(), name='nft'),
    path('nft_b/', getNFTView_b.as_view(), name='nft'),
]