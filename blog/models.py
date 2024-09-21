from django.db import models

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)
    email = models.EmailField()
    def __str__(self):
        return f"{self.first_name} {self.second_name}"

class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,null=True, related_name="posts")
    tag = models.ManyToManyField(Tag)