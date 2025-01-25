from django.test import TestCase
from django.urls import reverse
from .models import Post
from authors.models import Author
from tags.models import Tag
from catalogs.models import Catalog

class PostTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="John Doe", bio="A test author.")
        self.tag = Tag.objects.create(name="Technology")
        self.catalog = Catalog.objects.create(name="Tech News", description="Latest in tech.")
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
            author=self.author,
            catalog=self.catalog,
            slug="test-post",
        )
        self.post.tags.add(self.tag)

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    def test_post_search(self):
        response = self.client.get(reverse('post_list') + '?q=Test')
        self.assertContains(response, "Test Post")

    def test_post_filter_by_tag(self):
        response = self.client.get(reverse('post_list') + f'?tag={self.tag.name}')
        self.assertContains(response, "Test Post")

    def test_post_filter_by_catalog(self):
        response = self.client.get(reverse('post_list') + f'?catalog={self.catalog.id}')
        self.assertContains(response, "Test Post")
