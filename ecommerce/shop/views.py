from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import Product
from .models import Post
  
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

def index(request):
    datas={}
    return render(request, 'index.html', datas)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Votre compte a été créé avec succès.")
            return redirect('login')
        else:
            messages.error(request, "Une erreur s'est produite lors de la création de votre compte.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('index')  # Rediriger vers la page d'accueil après la connexion
        else:
            messages.error(request, "Une erreur s'est produite lors de la connexion.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('index')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('index')  # Rediriger vers la page d'accueil après la déconnexion

def about(request):
    datas = {}
    return render(request, 'about.html', datas) 


def contact(request):
    datas = {}
    return render(request, 'contact.html', datas) 

def forgot(request):
    datas = {}
    return render(request, 'forgot.html', datas) 

def menuArticle(request):
    products =  Product.objects.all()
    datas = {'products': products}
    return render(request, 'menuArticle.html', datas) 

def reset(request):
    datas = {}
    return render(request, 'reset.html', datas) 

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def blog_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blogDetail.html', {'post': post})


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer