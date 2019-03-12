from django.db import models

# Create your models here.

class Book(models.Model):
    """This class represents a book model"""
    title = models.CharField(max_length=255, blank=False)
    author = models.CharField(max_length=255, blank=False)
    copies = models.IntegerField(blank=False)
    date_added = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """Return a human readable representation of the book model"""
        return self.title
