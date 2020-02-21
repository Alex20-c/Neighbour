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
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    neighborhood = models.ForeignKey(Neighbourhood,null=True) 
    
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
     
    @receiver(post_save, sender=User) 
    def save_profile(sender,instance,**kwargs):
        instance.profile.save() 
        
        
    @classmethod
    def get_by_id(cls,id):
        profile = Profile.objects.get(user = id)
        return profile
    
    @classmethod
    def filter_by_id(cls,id): 
        profile = Profile.objects.filter(user = id).first()
        return profile
     
        
    def __str__(self):
        return self.title
    
class Business(models.Model):
    owner = models.CharField(max_length=40)
    business = models.CharField(max_length=200)
    business_email = models.EmailField(max_length=200)
    description = models.TextField(max_length=200)
    location = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE) 
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def create_business(self):
        self.save()
      
    def delete_business(self):
        self.delete()
        
    @classmethod
    def search_by_business(cls,search_term):
        businesses = cls.objects.filter(business__icontains=businesses)
        return businesses
    
    
    @classmethod
    def get_location_businesses(cls,location):
       businesses =Business.objects.filter(location__pk=location)

       return businesses
   
   

   
   
    @classmethod
    def get_profile_businesses(cls,user):
       business = Business.objects.filter(user__pk=user)
       print(business)
       return business
    
    def __str__(self):
        return self.owner
        
class Posts(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=200) 
    location = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def save_post(self):
        self.save()
    
    @classmethod
    def get_location_posts(cls,location):
        posts =Posts.objects.filter(location__pk=location)
        print(posts)
        return posts
    
    
    def __str__(self):
        return self.title
    
class Contacts(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    location = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    
    @classmethod
    def get_location_contacts(cls,location):
        contacts = Contacts.objects.filter(location__pk=location)
        return contacts
    
    def __str__(self):
        return self.name