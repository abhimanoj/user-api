from django.db import models
import time
import calendar
 
 
class UserTable(models.Model):
    first_name = models.CharField(max_length=100, default=None)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class UserDetailsTable(models.Model):
    email = models.CharField(max_length=100, default=None, unique=True)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user_table = models.ForeignKey(UserTable, related_name='user_table', on_delete=models.CASCADE)

