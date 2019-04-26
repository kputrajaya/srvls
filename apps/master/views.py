import json
import logging

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Log

logger = logging.getLogger(__name__)


class Ping(View):
    def get(self, request):
        return JsonResponse('Pong!', safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class Logs(View):
    def get(self, request):
        logs = Log.objects.order_by('-pk')[:100]
        data = [
            {
                'message': x.message,
                'image': x.image.url if x.image else None,
                'created_at': timezone.localtime(x.created_at)
            }
            for x in logs
        ]
        logger.info('Logs retrieved: {}'.format(json.dumps(data, cls=DjangoJSONEncoder)))
        return JsonResponse(data, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body)
            message = data['message']
        except (LookupError, json.JSONDecodeError):
            return HttpResponse(status=400)

        Log.objects.create(message=message)
        logger.info('Log created: {}'.format(json.dumps(data, cls=DjangoJSONEncoder)))
        return HttpResponse(status=201)
