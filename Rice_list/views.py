from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Rice_list(request):
    return HttpResponse('status=ok')