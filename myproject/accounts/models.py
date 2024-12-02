# from django.db import models

# se nao funcionar colocar o de cima tb
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

