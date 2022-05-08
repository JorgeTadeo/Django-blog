from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogposts/', views.BlogPostView.as_view(), name='blogposts'),
    path('blogpost/<int:pk>', views.BlogPostDetailView.as_view(), name='blog-post-detail'),
]
