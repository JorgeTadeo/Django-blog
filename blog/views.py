from django.shortcuts import render
from .models import Topic, BlogPost, Author, Comment
import django.views import generic

def index(request):
    """View function for home page of site."""

    num_blogposts = BlogPost.objects.count()
    num_authors = Author.objects.count()
    num_comments = Comment.objects.count()
    num_topics = Topic.objects.count()
    
    context = {
        'num_blogposts:': num_blogposts,
        'num_authors': num_authors,
        'num_comments': num_comments,
        'num_topics': num_topics,
    }

    return render(request, 'index.html', context=context)

class BlogPostView(generic.ListView):
    model = BlogPost