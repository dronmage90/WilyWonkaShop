from django.shortcuts import render
import json
from django.http.response import JsonResponse
from .models import Company,Product


def company_list(request):
    # select * from company;
    if request.method == 'GET':
        company = Company.objects.all()
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
        vacancy = Product.objects.filter(company=company)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    if request.method == 'GET':
        vacancy_json = [v.to_json() for v in vacancy]
        return JsonResponse(vacancy_json, safe=False)

def products_list(request):
    # select * from company;
    if request.method == 'GET':
        company = Product.objects.all()
        company_json = [p.to_json() for p in company]
        return JsonResponse(company_json, safe=False)


def product_one(request, vacancy_id):
    try:
        company = Product.objects.get(id=vacancy_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(company.to_json())

def products_list_top(request):
    # select * from company;
    if request.method == 'GET':
        company = Product.objects
        company_json = [p.to_json() for p in company]
        return JsonResponse(company_json, safe=False)


