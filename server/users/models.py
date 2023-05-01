from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20, blank=False, default='somevalue')
    created = models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return self.name