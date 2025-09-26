from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


def blog(request):
    posts = Post.objects.all().order_by('-created_at')  # أحدث مقالات أولاً
    return render (request , 'pages/blog.html', {'posts': posts})
    

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'page/post_detail.html', {'post': post})
