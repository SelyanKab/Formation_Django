from django.shortcuts import render,HttpResponse

# Create your views here.
def list_commande(request):
    return render(request,'commande/assuter.html')