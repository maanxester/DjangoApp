
from django.urls import path
from . import users

urlpatterns = [
    path('views', users.get_users, name='get_users'),
    path('view/<int:id>', users.get_user, name='get_user'),
    path('create', users.create_user, name='create_user'),
    path('delete/<int:id>', users.delete_user, name='delete_user'),
    path('update/<int:id>', users.update_user, name='update_user')
]
