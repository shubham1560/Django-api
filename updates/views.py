# import json
# from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from pure_django_api.mixins import JsonResponseMixin
from .models import Update
from django.core.serializers import serialize

# def detail_view(request):
#     return render()

# from .models import Update

# Create your views here.


def json_example_view(request):
    # URI -- for a REST Api
    # GET Request
    data = {
        "count": 1000,
        "content": "Some new Content"
    }
    """
    # for getting the response using python only
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type="application/json")
    
    """

    return JsonResponse(data)


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new Content"
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new Content"
        }
        return self.render_to_json_response(data)


class SerializedView(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        data = serialize("json", qs, fields=('user', 'content'))
        print(data)
        json_data = data
        return HttpResponse(json_data, content_type="application/json")