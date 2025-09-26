from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان المقال")
    # slug = models.SlugField(unique=True, blank=True, null=True, editable=False, verbose_name="الرابط") # 
    content = models.TextField(verbose_name="المحتوى")
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True, verbose_name="صورة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ النشر")

    def __str__(self):
        return self.title



    
