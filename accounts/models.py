from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField
from django.contrib.auth.models import User

class accounts(models.Model):
    first_name = CharField(max_length=200)
    last_name = CharField(max_length=200)
    age = IntegerField()
    address = CharField(max_length=200, blank=True)
    author = models.ForeignKey(User, on_delete=CASCADE, null=True)

    def __str__(self):
        return self.first_name