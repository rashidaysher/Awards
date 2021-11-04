from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from awards.models import *

# Create your tests here.


class Profile(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(
            username='developer',
            password='password'
        )
        self.neighborhood = Profile(
            name='Test Neighbourhood', location=self.location, occupants_count=100, admin_id=self.admin.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.neighborhood, Profile))

    def test_save_method(self):
        self.neighbourhood.create_neigborhood()
        neighborhoods = Profile.objects.all()
        self.assertTrue(len(neighborhoods) > 0)

    def test_delete_method(self):
        self.neighborhood.create_neigborhood()
        self.neighborhood.delete()
        neighborhoods = Profile.objects.all()
        self.assertTrue(len(neighborhoods) == 0)


class PostTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='dev-kev',
            password='password'
        )
        self.post = Project(title='Test Project', content='Test Content',
                         location=self.location, category=self.category, user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Project))

    def test_save_method(self):
        self.post.save()
        posts = Project.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_method(self):
        self.post.save()
        self.post.delete_post()
        posts = Project.objects.all()
        self.assertTrue(len(posts) == 0)