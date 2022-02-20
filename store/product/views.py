from django.http import Http404, JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .serializers import ProductSerializer
from .models import Product


@csrf_exempt
def product_list_api(request):
    if request.method == 'GET':
        product_serializer = ProductSerializer(Product.objects.all(), many=True)
        return JsonResponse({'data':product_serializer.data}, status=200)

    elif request.method == 'POST':
        data = request.POST
        product_serializer = ProductSerializer(data=data)
        if product_serializer.is_valid():
            new_product = product_serializer.save()
            return JsonResponse({'new_product_id': new_product.id}, status=201)
        else:
            return JsonResponse({'error': product_serializer.errors}, status=400)

    else:
        return JsonResponse({}, status=405)

