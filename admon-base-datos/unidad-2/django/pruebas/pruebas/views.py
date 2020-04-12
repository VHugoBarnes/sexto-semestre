from django.http import HttpResponse


def holamundo(request):
    return HttpResponse("¡Hola, mundo!")