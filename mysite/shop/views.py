from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Category, Product


def home(request):
    return HttpResponse("Hello, world. You are in home page.")

def categ(request):
    category_list = Category.objects.all()
    template = loader.get_template("shop/categories.html")
    context = {
        "category_list": category_list,
    }
    return HttpResponse(template.render(context, request))


def shop(request):
    return HttpResponse("Hello, world. You are in shop page.")
