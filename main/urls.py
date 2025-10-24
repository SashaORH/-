from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('projects', views.projects, name='projects'),
    path('faq', views.faq, name='faq'),
    path('contact', views.contact, name='contact'),
]