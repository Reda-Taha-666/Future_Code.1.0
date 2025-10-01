from django.contrib import admin
from django.urls import path , include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('jet/', include('jet.urls','jet')),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('contact/', include('contact.urls')),  # ربط تطبيق الفورم
    path('courses/', include('courses.urls')),  # ربط تطبيق الفورم
    path('library/', include('library.urls')),  # ربط تطبيق الفورم
    path('blog/', include('blog.urls')),  # ربط تطبيق الفورم



    path('success/', lambda request: render(request, "pages/success.html"), name='success'),


]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:  # عشان يشتغل في وضع التطوير فقط
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
