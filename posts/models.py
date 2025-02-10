from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=1200)
    content = models.CharField(max_length=1500)
    rete = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True ,null=True, blank=True)

def __str__(self):
    return f"{self.title} - {self.content}"
