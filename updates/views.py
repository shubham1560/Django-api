from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# def detail_view(request):
#     return render()

from .models import Update

# Create your views here.


def update_model_detail_view(request):
    # URI -- for a REST Api

    data = {
        "count": 1000,
        "content": "Some new Content"
    }
    return JsonResponse(data)