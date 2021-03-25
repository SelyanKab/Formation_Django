from django.http import HttpResponse
# Create your views here
def list_commande(request):
    return HttpResponse('la liste des commandes')