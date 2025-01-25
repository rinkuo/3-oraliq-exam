from django.db import models
from authors.models import Author
from tags.models import Tag
from django.utils.text import slugify
from django.urls import reverse
from catalogs.models import Category

STATUS_CHOICES = [
    ('draft', 'Draft'),
    ('published', 'Published'),
]

class Post(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    tag = models.ManyToManyField(Tag, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        else:
            original_slug = self.slug
            num = 1
            while Post.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{num}"
                num += 1
        super(Post, self).save(*args, **kwargs)


    def get_detail_url(self):
        return reverse('posts:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
