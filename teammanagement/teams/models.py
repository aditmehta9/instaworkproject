from django.db import models

# Create your models here.

CHOICES = [
    ('regular', "Regular - Can't delete members"),
    ('admin', 'Admin - Can delete members')
]


class Team(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"
