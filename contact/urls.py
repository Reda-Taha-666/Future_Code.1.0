from django.urls import path
from .views import contact_view
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
]
