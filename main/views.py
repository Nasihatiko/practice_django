from django.shortcuts import render
from django.http import HttpResponse
from main.models import Category, Product

# Create your views here.


def all_product(request):
    products = Product.objects.all()
    # SELECT * FROM Product
    return render(request, 'product.html', locals())


def category(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})
