from django.shortcuts import render
from services.models import Service

def services(request):

    services = Service.objects.all()

    ctx = {'services' : services}

    return render(request, "services/services.html", ctx)
