from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    context = {'test': 'test123'}
    return render(request, 'index.html', context)

def detail(request, insp_id):
    return JsonResponse(
        {
            'insp_id': insp_id,
            'details': 'Test detail',
        }
    )
