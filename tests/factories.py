import factory
from django.contrib.auth.models import User
from mainapp.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=Post
    
    password="test"
    username="test"
    is_superuser=True
    is_staff=True



class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=Post

    title="x"
    sub_title="x"
    slug="x"
    author=factory.SubFactory(User)
    content="x"
    status="Published"
    
