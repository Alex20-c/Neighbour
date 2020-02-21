from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Neighbourhood(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    count = models.IntegerField(default=0,blank=True) 
    
    def create_neighbourhood(self):
        self.save()
      
    def delete_neighbourhood(self):
        self.delete()
        
    @classmethod
    def find_by_id(cls,id):
        hoods = cls.objects.filter(id=id)
        return hoods  
    
    def __str__(self):
        return self.name
