import json

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Product, Category
from ..serializers import CategorySerializer1, ProductSerializer


@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


def product_list_rest(request):
    # select * from company;
    if request.method == 'GET':
        company = Category.objects.filter(home=False)
        product = Product.objects.filter(category__in=company)
        product_json = [p.to_json() for p in product]
        return JsonResponse(product_json, safe=False)


def product_list_home(request):
    # select * from company;
    if request.method == 'GET':
        company = Category.objects.filter(home=True)
        product = Product.objects.filter(category__in=company)
        product_json = [p.to_json() for p in product]
        return JsonResponse(product_json, safe=False)


def product_by_category(request, category_id):
    # select * from company;
    if request.method == 'GET':
        company = Category.objects.filter(id=category_id)
        product = Product.objects.filter(category__in=company)
        product_json = [p.to_json() for p in product]
        return JsonResponse(product_json, safe=False)


@api_view(['POST'])
def do_product(request):
    # select * from company;
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name', '')
        price = data.get('price', '')
        cid = data.get('cid', '')
        r = Category.objects.get(id=cid)
        a = Product(name=name, price=price, category=r)
        a.save()
        return JsonResponse(a.to_json(), safe=False)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response({'deleted': True})
