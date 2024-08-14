from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nslides = n//4 +ceil((n/4)-(n//4))
    data = {'no_of_slides':nslides,'range':range(1,nslides),'products':products}
    return render(request,'eshop/index.html', data)

def about(request):
    return render(request,'eshop/about.html')

def contact(request):
    return HttpResponse("This is the contact page")

def tracker(request):
    return HttpResponse("This is the contact page")

def search(request):
    return HttpResponse("This is the search page")

def productView(request):
    return HttpResponse("This is the product view page")

def checkout(request):
    return HttpResponse("This is the checkout page")