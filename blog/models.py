from tkinter import CASCADE
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
    # A blog post may only have one author but many authors can have many blog posts
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    # A text field that holds the contents of our blog post
    description = models.TextField(max_length=1000, help_text='Enter a description for you post')
    # A Blog Post can have many topics and a topic can be applied to many blog posts
    topic = models.ManyToManyField(Topic, help_text='Select a topic for this blog post')

    class Meta:
        # order the blog posts in reverse cronological order
        ordering = ['-post_date']
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.title} - {self.author.user}'
    
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

class Comment(models.Model):
    # Every comment must have an Author and Authors can have many comments
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    # A text field of what comment is 
    description = models.TextField(max_length=300, help_text='Enter comment about blog here')
    # A blog post the comment refers too
    blogpost =models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    class Meta:
        # order the comments in cronological order according to post date
        ordering=['post_date']
    
    def __str__(self):
        """String for representing Comment object."""
        return f'{self.post_date} - {self.author.user} - {self.description}'