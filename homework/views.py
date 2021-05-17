from django.http import HttpResponse
from django.shortcuts import render, redirect
from homework.models import Product, Review
# Create your views here.

def get_all_product(request):
    word = request.Get.get('search', '')
    product = Product.objects.filter(name__contains=word)
    print(product)
    data = {
        'all_product' : product
    }
    return render(request, 'product.html', context=data)


def get_one_product(request, id):
    product = Product.objects.get(id=id)
    reviews = Review.objects.filter(product_id=id)
    data = {
        'product': product,
        'reviews': reviews
    }
    return render(request, 'detail.html', context=data)


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('product_name', '')
        Product.objects.create(name=name)
        return redirect('/product/')
    return render(request, 'add.html')