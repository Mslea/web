from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title
    