from django.db import models

class About(models.Model):
    Name = models.CharField(max_length = 100)
    LastName = models.CharField(max_length = 100)
    Age = models.IntegerField()
    Email = models.CharField(max_length = 100)
    PhoneNumber = models.CharField(max_length = 100)
    Address = models.CharField(max_length = 300)

