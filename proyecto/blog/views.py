from django.shortcuts import render
from .models import Post, Categoria

# Create your views here.
def blog(request):
    post = Post.objects.all()
    categoria= Categoria.objects.all()
    return render(request,'blog/blog.html',{'post':post,'categoria':categoria})

def categoria(request,categotia_id):
    categoria= Categoria.objects.get(id=categotia_id)
    post = Post.objects.filter(categorias=categoria)
    return render(request,'blog/categoria.html',{'post':post,'categoria':categoria})
