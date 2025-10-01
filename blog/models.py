from django.db import models
# from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان المقال")
    # slug = models.SlugField(unique=True, blank=True, null=True, editable=False, verbose_name="الرابط") # 
    content = models.TextField(verbose_name="المحتوى")
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True, verbose_name="صورة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ النشر")

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)   # اسم المستخدم بدل login
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"