from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.


def blog(request):
    posts = Post.objects.all().order_by('-created_at')  # أحدث مقالات أولاً
    return render (request , 'pages/blog.html', {'posts': posts})
    


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by("-created_at")

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'page/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })