from django.http import HttpResponse

def view_a(request):
    return HttpResponse(request, 'view_a.html')

def view_b(request):
    return HttpResponse(request, 'view_b.html')