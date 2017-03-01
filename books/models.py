from django.db import models
from django.utils.timezone import now

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=150)
    author = models.ManyToManyField("Author", related_name="Books")
    review = models.TextField(blank=True, null=True)
    date_reviewed = models.DateTimeField(blank=True, null=True)
    is_favorite = models.BooleanField(default=False, verbose_name="Favorite?")

    #Title/Author return method
    def __str__(self):
        return self.title

    def list_authors(self):
        return ", ".join([author.name for author in self.authors.all])

    def save(self, *args, **kwargs):
        if (self.review and self.date_reviewed is None):
            self.date_reviewed=now()

        super(Book,self).save(*args, **kwargs)

class Author(models.Model):
    name = models.CharField(max_length=70 , help_text="Use pen name, not real name.")

    def __str__(self):
        return self.name
