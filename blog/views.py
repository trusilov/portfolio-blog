from django.shortcuts import render, get_object_or_404

from .models import Post


def allblogs(request):
    posts = Post.objects
    return render(request, 'blog/allblogs.html', {'posts': posts})


def detail(request, post_id):
    detailpost = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': detailpost})


