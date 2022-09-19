from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from company.models import CompanyModel
from company.serializers import CompanySerializer


@csrf_exempt
def CompanyApi(request):
    if request.method == 'GET':
        companies = CompanyModel.objects.all()
        companies_serializer = CompanySerializer(companies, many=True)
        return JsonResponse(companies_serializer.data, safe=False)
    elif request.method == 'POST':
        company_data = JSONParser().parse(request)
        companies_serializer = CompanySerializer(data=company_data)
        if companies_serializer.is_valid():
            companies_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method == 'PUT':
        company_data = JSONParser().parse(request)
        company = CompanyModel.objects.get(CompanyID=company_data['CompanyID'])
        companies_serializers = CompanySerializer(company, data=company_data)
        if companies_serializers.is_valid():
            companies_serializers.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to Update')
    elif request.method == 'DELETE':
        company = CompanyModel.objects.get()
        company.delete()
        return JsonResponse('Deleted Successfully', safe=False)
