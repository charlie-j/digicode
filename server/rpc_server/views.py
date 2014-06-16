# -*- coding: utf-8 -*-

from functools import wraps
from django.views.decorators.csrf import csrf_exempt

from digicode.models import Code, Local

#from django.http import JsonResponse
#L'import précédent ne marche pas avant django 1.7. On recode JsonResponse à
#la main (sic)
# <kludge>
from django.http import HttpResponse
import json

class JsonResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        super(JsonResponse, self).__init__(json.dumps(data),  **kwargs)
# </kludge>

def register(request):
    """Appelé la première fois qu'un digicode s'initialise. Renvoie
    le json de sa configuration (histoire qu'il s'autoconfigure)
    """
    raise NotImplementedError

def authenticate(request):
    """Check shared secret et id d'un digicode"""
    try:
        return Local.objects.get(pk=request.POST.get('id',0),
            shared_secret__exact=request.POST.get('shared_secret',''))
    except Local.DoesNotExist:
        return None

@csrf_exempt
def code(request):
    """Appelé lorsque le digicode a reçu quelque chose"""
    if set(request.POST.dict().keys()) != set(['id', 'shared_secret', 'code']):
        return JsonResponse({'open': False}, status=400)

    local = authenticate(request)
    if not local:
        return JsonResponse({'open': False}, status=403)
    
    # Normal usage here
    return JsonResponse({'open': local.try_code(request.POST.get('code', ''))})
    
