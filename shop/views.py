from django.shortcuts import render
from.models import Producct

def index(request):
    product=Producct.objects.all()
    return render(request,"index.html",{'product':product}),
def product(request):
    product=Producct.objects.all()
    return render(request,"product.html",{'product':product})
