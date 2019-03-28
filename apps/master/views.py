import json

from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Log


@method_decorator(csrf_exempt, name='dispatch')
class Logs(View):
    def get(self, request):
        logs = Log.objects.order_by('-pk')[0:100]
        data = [
            {
                'message': x.message,
                'image': x.image.url if x.image else None,
                'created_at': x.created_at
            }
            for x in logs
        ]
        return JsonResponse(data, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body)
            message = data['message']
        except (LookupError, json.JSONDecodeError):
            return HttpResponse(status=400)

        Log.objects.create(message=message)
        return HttpResponse(status=201)
