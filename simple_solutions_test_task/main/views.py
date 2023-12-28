from decimal import Decimal

from django.shortcuts import get_object_or_404, render
from django.views import View
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from .models import Item
from .serializers import ItemModelSerializer
from .utils import stripe_session_create


class GetStripeSessionIdView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemModelSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        obj_id = kwargs.get('id')
        obj = self.queryset.get(id=obj_id)
        session_id = stripe_session_create(obj)
        return Response(status=status.HTTP_200_OK, data=session_id)


class CreateItem(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemModelSerializer


class GetItem(View):
    template_name = 'item_page.html'

    def get(self, request, id, *args, **kwargs):
        item_obj = get_object_or_404(Item, id=id)
        context = {'item': item_obj}

        return render(request, self.template_name, context)
