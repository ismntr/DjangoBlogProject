from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import PostForm


def post_list(request):
    if request.user.is_authenticated:
        # Eğer kullanıcı giriş yapmışsa, kendi postlarını listeleyelim
        posts = Post.objects.filter(is_deleted=False, user=request.user)
    else:
        # Kullanıcı giriş yapmamışsa, tüm postları listeleyelim
        posts = Post.objects.filter(is_deleted=False)

    return render(request, 'myapp/post_list.html', {'posts': posts})


def post_detail(request, pk):
    return HttpResponse(f"Post Detail for Post ID: {pk}")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            kullanici = form.save()
            login(request, kullanici)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            kullanici = authenticate(username=username, password=password)
            if kullanici is not None:
                login(request, kullanici)
                return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def logout(request):
    logout(request)
    return redirect('login')



def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
        
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    
    return render(request, 'myapp/post_create.html', {'form': form})


