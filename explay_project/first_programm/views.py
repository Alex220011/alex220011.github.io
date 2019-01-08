from django.shortcuts import render, get_object_or_404

# Create your views here.
from first_programm.models import Name


def popi(request):
    fop = Name.objects.all()
    return render(request, "sasha.html", dict(objects=fop))

def rilize(request, id):
    riliz = get_object_or_404(Name, id=id)
    return render(request, "relese.html", dict(object=riliz))
