from django.shortcuts import render

def photo(request):

    return render(request, 'index.html', {})


def photoCreate(req):

    return None