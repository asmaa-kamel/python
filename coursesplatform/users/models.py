from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=200, unique=True)
    age = models.SmallIntegerField()

    def __str__(self):
        return self.user.username