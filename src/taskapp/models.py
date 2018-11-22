from django.db import models

# Create your models here.

class Contact(models.Model):
    owner=models.ForeignKey('auth.User',on_delete=models.CASCADE,null=True,blank=True)
    name  = models.CharField(max_length=100)

    def __str__(self):
        return self.name