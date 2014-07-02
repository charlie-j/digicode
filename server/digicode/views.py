from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from models import Code

@login_required
def liste(request):
    return render(request, "liste.html", {
        'liste': Code.objects.all().filter(proprietaire=request.user),
    })
# Create your views here.
