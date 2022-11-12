from django.shortcuts import render


def index(request):
    context = {
        'title': 'BelPackImport'
    }
    return render(request, 'belpackimport/index.html', context)
