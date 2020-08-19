from django.shortcuts import render,get_object_or_404
from .models import Category, Picture
from django.http import HttpResponse

# Create your views here.
def picture_list(request):
    categories = Category.objects.all()
    pictures = Picture.objects.filter()


def picture_detail(request, id):
    picture=Picture.objects.get(id=id)
    return render(request,'Pictures/picture/detail.html',{'picture': picture})
    return render(request, 'list.html',{'categories': categories,'pictures': pictures})
def index(request):
    return HttpResponse("Hello, world. You're at the picture_list.")    