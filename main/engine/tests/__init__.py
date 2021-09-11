
from django.test import TestCase, RequestFactory, Client
from engine.web.models import User, Group


def create_user():
    user = User(name="name", password="password", admin=False)
    user.save()
    return user.id


class ProjectTest(TestCase):
    def setUp(self):
        User.objects.create(name="test", password="teste", admin=False)
