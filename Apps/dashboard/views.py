from django.shortcuts import render

# Create your views here.

def dashboard(request):
    data = {
        'name': 'Bryan',
        'surname': 'Urbina',
        'title': 'HOME | DOXER'
    }
    return render(request, 'dashboard.html', data)