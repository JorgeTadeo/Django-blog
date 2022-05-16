from django.shortcuts import render
from .models import Topic, BlogPost, Author, Comment
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import get_object_or_404

def index(request):
    """View function for home page of site."""

    num_blogposts = BlogPost.objects.count()
    num_authors = Author.objects.count()
    num_comments = Comment.objects.count()
    num_topics = Topic.objects.count()
    
    context = {
        'num_blogposts': num_blogposts,
        'num_authors': num_authors,
        'num_comments': num_comments,
        'num_topics': num_topics,
    }

    return render(request, 'index.html', context=context)

class BlogPostView(generic.ListView):
    model = BlogPost
    paginate_by = 10

class BlogPostDetailView(generic.DetailView):
    model = BlogPost

class AuthorsListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['description']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        # Get the blogger object from the "pk" URL parameter and add it to the context
        context['blogpost'] = get_object_or_404(BlogPost, pk = self.kwargs['pk'])
        return context

    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user
        #Associate comment with blog based on passed id
        form.instance.blogpost=get_object_or_404(BlogPost, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(CommentCreateView, self).form_valid(form)

    def get_success_url(self): 
        """
        After posting comment return to associated blog.
        """
        return reverse('blog-post-detail', kwargs={'pk': self.kwargs['pk'],})