from django.db import models
from person.models import Person
from passlib.hash import pbkdf2_sha256

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=200, default="")
    person_id = models.OneToOneField(Person, on_delete=models.CASCADE, null=True)

    def verifify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)
