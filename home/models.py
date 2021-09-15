from django.db import models

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    desc = models.TextField()
    def __str__(self):
        return self.name
    