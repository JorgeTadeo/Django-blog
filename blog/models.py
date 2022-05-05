from django.db import models

# Create your models here.
class Topic(models.Model):
    """Model representing a blog topic."""
    name = models.CharField(max_length=200, help_text='Enter a blog topic (e.g Technology')

    def __str__(self):
        """String for representing the Model Object."""
        return self.name
