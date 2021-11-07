from django.shortcuts import render

# Create your views here.

def dashboard(request):
    data = {
        'name': 'Bryan',
        'surname': 'Urbina'
    }
    return render(request, 'dashboard.html', data)