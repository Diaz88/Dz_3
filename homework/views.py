from django.http import HttpResponse
from django.shortcuts import render, redirect

from homework.forms import ProductForm, UserCreationForm
from homework.models import Product, Category


# Create your views here.

def get_all_product(reguest):
    word = reguest.GET.get('search', '')
    product = Product.objects.filter(name__contains=word)
    data = {
        'all_product': product
    }
    return render(reguest, 'product.html', context=data)


def get_one_product(request, id):
    product = Product.objects.get(id=id)
    category = Category.objects.filter(product_id=id)
    data = {
        'product': product,
        'category': category
    }
    return render(request, 'detail.html', context=data)


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('product_name', '')

        Product.objects.create(name=name)
        return redirect('/product/')
    return render(request, 'add.html')


def add(request):
    if request.method == 'POST':
        print(request.POST)
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/product/')
        else:
            return render(request, 'add1.html', context={
                'form': form
            })
    data = {
        'form': ProductForm()
    }
    return render(request, 'add1.html', context=data)

def main_page(request):
    return render(request, "main.html")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            print('POST запрос без ошибок')
            return redirect('/admin/')
        else:
            print('POST запрос с ошибкой')
            return render(request, 'register.html', context={'form': form })

    data = {
        'form': UserCreationForm()
    }
    print('GET запрос')
    return render(request, 'register.html', context=data)

