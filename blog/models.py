from django.db import models
from django.urls import reverse

# Create your models here.
class Topic(models.Model):
    """Model representing a blog topic."""
    name = models.CharField(max_length=200, help_text='Enter a blog topic (e.g Technology')

    def __str__(self):
        """String for representing the Model Object."""
        return self.name

class BlogPost(models.Model):
    """Model representing a blog post."""
    title = models.CharField(max_length=200)
    post_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text='Enter a description for you post')
    topic = models.ManyToManyField(Topic, help_text='Select a topic for this blog post')

    class Meta:
        ordering = ['-post_date']
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this post."""
        return reverse('blog-post-detail', args=[str(self.id)])

class Author(models.Model):
    user = models.CharField(max_length=200)
    bio = models.TextField(max_length=1000, help_text='Enter a biography')

    class Meta:
        ordering=['user']

    def __str___(self):
        """String for representing Author object."""
        return self.user
    
    def get_absolute_url(self):
        """Returns the URL to access a deatil record for this user."""
        return reverse('author-detail', args=[str(self.id)])
