from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='author_profiles/', null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=200)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username