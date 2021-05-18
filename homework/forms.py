from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput

from homework.models import Product


class ProductForm(forms.Form):
     name = forms.CharField(min_length=2, max_length=10,
                               required = True, label='Продукт',
                           widget=TextInput(attrs={
                               'placeholder': 'Название продукта'
                           }))

     def clean_name(self):
         name = self.cleaned_data['name']
         print(name)
         product = Product.objects.filter(name=name)
         print(product.count())
         if product.count() > 0:
             raise ValidationError('Такое слово уже существует!!!')
         return name

     def save(self, commit=True):
         product = Product.objects.create(name=self.cleaned_data['name'])
         product.save()
         return product