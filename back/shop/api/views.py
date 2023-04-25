from django.shortcuts import render
import json
from django.http.response import JsonResponse
from .models import Company, Product


def company_list(request):
    # select * from company;
    if request.method == 'GET':
        company = Company.objects.all()
        company_json = [p.to_json() for p in company]
        return JsonResponse(company_json, safe=False)


def company_list_home(request):
    # select * from company;
    if request.method == 'GET':
        company = Company.objects.filter(homeMade=True)
        company_json = [p.to_json() for p in company]
        return JsonResponse(company_json, safe=False)


def company_list_rest(request):
    # select * from company;
    if request.method == 'GET':
        company = Company.objects.filter(homeMade=False)
        company_json = [p.to_json() for p in company]
        return JsonResponse(company_json, safe=False)


def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(company.to_json())


def products_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
        product = Product.objects.filter(company=company)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    if request.method == 'GET':
        product_json = [v.to_json() for v in product]
        return JsonResponse(product_json, safe=False)


def products_list(request):
    # select * from company;
    if request.method == 'GET':
        company = Product.objects.all()
        company_json = [p.to_json() for p in company]
        return JsonResponse(company_json, safe=False)


def product_one(request, product_id):
    try:
        company = Product.objects.get(id=product_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(company.to_json())


def products_list_top(request):
    if request.method == 'GET':
        product = Product.objects
        product_json = [p.to_json() for p in product]
        return JsonResponse(product_json, safe=False)


def products_list_home(request):
    if request.method == 'GET':
        company = Company.objects.filter(homeMade=True)
        product = Product.objects.filter(company__in=company)
        product_json = [p.to_json() for p in product]
        return JsonResponse(product_json, safe=False)


def products_list_rest(request):
    if request.method == 'GET':
        company = Company.objects.filter(homeMade=False)
        product = Product.objects.filter(company__in=company)
        product_json = [p.to_json() for p in product]
        return JsonResponse(product_json, safe=False)
