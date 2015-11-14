from django.http import HttpResponse
from .models import Item


def index(request):
    return HttpResponse(len(Item.objects.all()))
