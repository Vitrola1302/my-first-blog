from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path(route='', view = views.about, name='About'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]