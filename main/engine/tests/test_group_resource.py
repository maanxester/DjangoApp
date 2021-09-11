from django.db import connection

from django.test import TestCase, RequestFactory
from engine.web.models import User, Group


class ProjectTest(TestCase):
    def setUp(self):
        User.objects.create(name="test", password="teste", admin=False)
