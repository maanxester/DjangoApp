from django.db import models
from werkzeug.security import generate_password_hash, check_password_hash


class User(models.Model):
    name = models.CharField(max_length=80, unique=True, null=False)
    password_hash = models.CharField(max_length=120)
    admin = models.BooleanField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<User %r' % self.name

    @property
    def serialized(self):
        return {
            'id': self.id,
            'name': self.name,
            'admin': self.admin

        }

    @property
    def password(self):
        raise AttributeError('Hidden Password')

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def verify_password(self, value):
        return check_password_hash(self.password_hash, value)


class Group(models.Model):
    name = models.CharField(max_length=80, unique=True, null=False)
    user = models.ManyToManyField(User, blank=True)

    def __repr__(self):
        return '<Group %r' % self.user

    @property
    def serialized(self):
        return {
            'name': self.name,
            'users': [
                {
                    'id': user.id,
                    'name': user.name
                }
                for user in self.user
            ]
        }
