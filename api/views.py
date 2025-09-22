from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Item


def hello(request):
    return JsonResponse({"message": "hello world"})


@csrf_exempt
def create_item(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('Only POST allowed')
    try:
        payload = json.loads(request.body or b"{}")
        name = payload.get('name')
        if not name:
            return JsonResponse({"error": "'name' is required"}, status=400)
        item = Item.objects.create(name=name)
        return JsonResponse({"id": item.id, "name": item.name, "created_at": item.created_at.isoformat()})
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

# Create your views here.
