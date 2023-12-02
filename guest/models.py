from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Guest(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    to_see = models.CharField(max_length=100)
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    has_signed_out = models.BooleanField(default=False)
    