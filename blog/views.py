from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Post


def blogs(request):
    posts = Post.objects.all()

    return render(request, 'blog/blogs.html', context={'posts': posts})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'blog/detail.html', context={'post': post})
