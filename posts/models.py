from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'


class Tag(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    class Heta:
        verbose_name_plural = 'Tags'
        verbose_name = 'Tag'


class Post(models.Model):
    image = models.ImageField(null=True, blank=False)
    title = models.CharField(max_length=1200)
    content = models.CharField(max_length=1500)
    rete = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True ,null=True, blank=True)

category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='category', null=True, blank=True)
tag = models.ManyToManyField(Tag,related_name='tag', blank=True,null=True)
def __str__(self):
    return f"{self.title} - {self.content}"

class Meta:
    verbose_name_plural = 'Posts'
    verbose_name = 'Post'
