from django.shortcuts import render


#Vista para la pagina de inicio, se renderiza el template index.html
def index (request):
    return render(request, "index.html", {'price': 100})
