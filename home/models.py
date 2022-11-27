from django.db import models

class Player(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    age = models.IntegerField()
    

    def __str__(self):
        return self.last_name
