import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    req_body = json.loads(request.body.decode())
    try:
        new_user = User.objects.create_user(
            username = req_body['username'],
            password = req_body['password']
        )
        token = Token.objects.create(user=new_user)
        data = json.dumps({'token': token.key})
        return HttpResponse(data, content_type='application/json')
    except Exception:
        data = json.dumps({})
        return HttpResponse(data, content_type='application/json')
