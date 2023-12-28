from django.urls import path
from .views import GetStripeSessionIdView, CreateItem

urlpatterns = [
    path('buy/<int:id>/', GetStripeSessionIdView.as_view(), name='buy-detail'),
    path('item/create', CreateItem.as_view(), name='item-create')
]