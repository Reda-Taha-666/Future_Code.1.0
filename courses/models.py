from django.db import models
from django.db.models import Max
from urllib.parse import urlparse, parse_qs


# from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان الكورس")
    description = models.TextField(verbose_name="المحتوى")
    cover_image = models.ImageField(upload_to='courses/', blank=True, null=True, verbose_name="صورة")
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    duration = models.CharField(max_length=50,null=True)            # المدة (مثلا 10 ساعات)
    level = models.CharField(max_length=50,null=True, choices=[
        ('beginner', 'مبتدئ'),
        ('intermediate', 'متوسط'),
        ('advanced', 'متقدم'),
    ])
    language = models.CharField(max_length=50, default="العربية",null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00,null=True)
    


    class Meta:
        ordering = ['created_at']   # بالتصاعدي (الأقدم فوق – الجديد تحت)
    


    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video_url = models.URLField()  # لينك YouTube
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.order == 0:  # لو ما كتبتش رقم
            last_order = Lesson.objects.filter(course=self.course).aggregate(models.Max("order"))["order__max"] or 0
            self.order = last_order + 1
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["order", "id"]  # يرتب حسب order أولاً

    @property
    def video_id(self):
        url = (self.video_url or "").strip()
        if not url:
            return ""

        # لو المستخدم أدخل الـ ID فقط
        if '/' not in url and 'youtube' not in url and 'youtu.be' not in url:
            return url.split('?')[0]

        parsed = urlparse(url)

        # short link: youtu.be/ID
        if parsed.netloc.endswith("youtu.be"):
            return parsed.path.lstrip("/").split("?")[0]

        # standard youtube.com links
        if "youtube" in parsed.netloc:
            # مثال: ?v=ID
            qs = parse_qs(parsed.query)
            if "v" in qs:
                return qs["v"][0].split("&")[0]
            # ممكن يكون /embed/ID أو /watch/ID
            parts = parsed.path.split("/")
            if parts:
                return parts[-1].split("?")[0]

        # fallback بسيط: آخر جزء قبل الاستعلام
        return url.split("/")[-1].split("?")[0]

    def __str__(self):
        return f"{self.course.title} - {self.title}"




# class Course(models.Model):
#     title = models.CharField(max_length=200)              # اسم الدورة
#     short_description = models.CharField(max_length=300)  # وصف قصير
#     description = models.TextField()                      # وصف تفصيلي
#     cover_image = models.ImageField(upload_to="courses/") # صورة الكورس
#     instructor = models.ForeignKey(User, on_delete=models.CASCADE) # المدرّس
#     duration = models.CharField(max_length=50)            # المدة (مثلا 10 ساعات)
#     level = models.CharField(max_length=50, choices=[
#         ('beginner', 'مبتدئ'),
#         ('intermediate', 'متوسط'),
#         ('advanced', 'متقدم'),
#     ])
#     language = models.CharField(max_length=50, default="العربية")
#     price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
#     created_at = models.DateTimeField(auto_now_add=True)

    
#     def __str__(self):
#         return self.title
