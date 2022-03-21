from rest_framework.response import Response
from rest_framework import permissions, generics, authentication
from rest_framework.views import APIView
from .models import User, Address
from .serializers import AddressSerializer, CustomerSerializer


class AddressListApi(APIView):

    def get(self, request):
        address_serializer = AddressSerializer(Address.objects.all(), many=True)
        return Response(address_serializer, status=200)

    def post(self, request):
        address_serializer = AddressSerializer(data=request.POST)
        if address_serializer.is_valid():
            new_address = address_serializer.save()
            return Response({'new_address_id': new_address.id}, status=201)
        else:
            return Response({'errors': address_serializer.errors}, status=400)


class CustomerListApi(APIView):

    def get(self, request):
        customer_serializer = CustomerSerializer(User.objects.all(), many=True)
        return Response(customer_serializer, status=200)

    def post(self, request):
        customer_serializer = CustomerSerializer(data=request.POST)
        if customer_serializer.is_valid():
            new_customer = customer_serializer.save()
            return Response({'new_customer_id': new_customer.id}, status=201)
        else:
            return Response({'errors': customer_serializer.errors}, status=400)


class CustomerDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]
