# from django.db import models
from django.contrib.auth.models import AbstractUser

# Userを抽象化したやつを使う

class CustomUser(AbstractUser):

    pass