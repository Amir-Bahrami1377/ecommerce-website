from rest_framework.response import Response
from rest_framework import permissions, generics, authentication
from rest_framework.views import APIView
from order.models import OrderItem, Order, OffCode
from .serializers import OrderSerializer, OrderItemSerializer, OffCodeSerializer


# class OrderItemListCreateApi(APIView):
#
#     def get(self, request):
#         order_item_serializer = OrderItemSerializer(OrderItem.objects.all(), many=True)
#         return Response({'data': order_item_serializer}, status=200)
#
#     def post(self, request):
#         order_item_serializer = OrderItemSerializer(data=request.POST)
#         if order_item_serializer.is_valid():
#             new_address = order_item_serializer.save()
#             return Response({'new_orderitem_id': new_address.id}, status=201)
#         else:
#             return Response({'errors': order_item_serializer.errors}, status=400)


class OrderItemListCreateApi(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
