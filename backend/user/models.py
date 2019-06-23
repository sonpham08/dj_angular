from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    fullname = models.CharField(max_length=255)
    is_staff_gun = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    phone = models.CharField(max_length=12,default='unknow')
    address = models.CharField(max_length=255, default='unknow')
    cmnd = models.CharField(max_length=15, default='unknow')

class Logging(models.Model):
    logging_id = models.AutoField(primary_key=True)
    date_logging = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)