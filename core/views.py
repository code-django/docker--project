from django.http import HttpResponse

def home(request):
    return HttpResponse("welcome in docker enviroment")