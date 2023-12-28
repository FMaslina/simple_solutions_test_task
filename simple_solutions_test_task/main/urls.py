from django.urls import path
from .views import GetStripeSessionIdView, CreateItem, GetItem

urlpatterns = [
    path('buy/<int:id>/', GetStripeSessionIdView.as_view(), name='buy-detail'),
    path('item/create', CreateItem.as_view(), name='item-create'),
    path('item/get/<int:id>', GetItem.as_view(), name='item-get')
]
