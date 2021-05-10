import json
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

@csrf_exempt
def login(request):
    req_body = json.loads(request.body.decode())

    if request.method == 'POST':
        username = req_body['username']
        password = req_body['password']
        authenticated_user = authenticate(username=username, password=password)

        if authenticated_user is not None:
            token = Token.objects.get(user=authenticated_user)
            data = json.dumps({'token': token.key, 'user_id': authenticated_user.id, 'username': authenticated_user.username})
            return HttpResponse(data, content_type='application/json')
        else:
            data = json.dumps({})
            return HttpResponse(data, content_type='application/json')
