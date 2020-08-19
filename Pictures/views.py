from django.shortcuts import render,get_object_or_404
from .models import Category, Picture

# Create your views here.
def picture_list(request):
    categories = Category.objects.all()
    pictures = Picture.objects.filter()
    return render(request, 'list.html',{'categories': categories,'pictures': pictures})


def picture_detail(request, id):
    picture=Picture.objects.get(id=id)
    return render(request,'Pictures/picture/detail.html',{'picture': picture})

