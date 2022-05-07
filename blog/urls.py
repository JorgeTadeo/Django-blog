from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogposts/', views.BlogPostView.as_view(), name='blogposts'),
]
