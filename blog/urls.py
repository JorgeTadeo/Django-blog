from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogposts/', views.BlogPostView.as_view(), name='blogposts'),
    path('blogpost/<int:pk>', views.BlogPostDetailView.as_view(), name='blog-post-detail'),
    path('authors/', views.AuthorsListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('blogpost/<int:pk>/comment/', views.CommentCreateView.as_view(), name='blog_comment')
]
