from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden 
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import PostForm

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.user != request.user:
        return HttpResponseForbidden("You do not have permission to access this post.")
    return render(request, 'myapp/post_detail.html', {'post': post})

def post_list(request):
    if request.user.is_authenticated:
        # Eğer kullanıcı giriş yapmışsa, kendi postlarını listeleyelim
        posts = Post.objects.filter(is_deleted=False, user=request.user)
    else:
        # Kullanıcı giriş yapmamışsa, tüm postları listeleyelim
        posts = Post.objects.filter(is_deleted=False)

    return render(request, 'myapp/post_list.html', {'posts': posts})


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.user != request.user:
        return HttpResponseForbidden("You do not have permission to access this post.")
    return render(request, 'myapp/post_detail.html', {'post': post})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):  
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)  
                return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):  
    auth_logout(request)  
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

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)
    if request.method == 'POST':
        post.is_deleted = not post.is_deleted
        post.save()
    return redirect('post_detail', pk=pk)


@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.user != request.user:
        return HttpResponseForbidden("You do not have permission to update this post.")
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'myapp/post_form.html', {'form': form})
