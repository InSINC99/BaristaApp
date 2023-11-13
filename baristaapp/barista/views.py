from django.shortcuts import HttpResponse
from .models import *
from django.core.serializers import serialize

def get_beans(request):
    data = Beans.objects.all()
    serialized_data = serialize('json', data)
    return HttpResponse(serialized_data, content_type='application/json')

def get_source(request):
    data = Source.objects.all()
    serialized_data = serialize('json', data)
    return HttpResponse(serialized_data, content_type='application/json')