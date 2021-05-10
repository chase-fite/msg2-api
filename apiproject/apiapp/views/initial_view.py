from django.http import HttpResponse

def initial(request):
    return HttpResponse('Initial view')
