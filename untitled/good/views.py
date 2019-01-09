from django.shortcuts import render, get_object_or_404

from good.models import Store

def home_page(request):
    return render(request, 'good/home-page.html')

def home(request):
    store_list = Store.objects.all()
    return render(request, 'good/home.html', dict(objects=store_list))


def start_visit(request, id):
    store = get_object_or_404(Store, id=id)
    return render(request, 'good/visit.html', dict(object=store))
