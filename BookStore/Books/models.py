from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE
    )

    def _str_(self):
        return self.title
