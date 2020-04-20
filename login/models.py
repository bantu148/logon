from django.db import models

# Create your models here.
class user(models.Model):
    user_id = models.AutoField
    user_email = models.CharField(max_length=30)
