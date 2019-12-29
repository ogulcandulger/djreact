from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return self.title 