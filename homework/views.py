from django.http import HttpResponse
from django.shortcuts import render
from homework.models import Product
# Create your views here.

def get_all_product(request):
    product = Product.objects.all()
    data = {
        'all_product' : product
    }
    return render(request, 'product.html', context=data)


def get_one_product(request, id):
    product = Product.objects.get(id=id)
    data = {
        'product' : product
    }
    return render(request, 'detail.html', context=data)