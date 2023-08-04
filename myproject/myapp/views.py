from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def post_list(request):
    posts = Post.objects.filter(is_deleted=False)
    #return render(request, 'post_list.html', {'posts': posts})
    return render(request, 'myapp/post_list.html', {'posts': posts})


def post_detail(request, pk):
    # Burada post detayını almak için gerekli işlemleri yapın
    return HttpResponse(f"Post Detail for Post ID: {pk}")




    
