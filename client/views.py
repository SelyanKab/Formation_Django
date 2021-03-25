from django.http import HttpResponse
# Create your views here
def list_client(request):
    return HttpResponse('la liste des clients')
