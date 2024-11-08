from django.db import models

# Create your models here.
class Pet(models.Model):
    name=models.CharField(max_length=100)
    pet_type=models.CharField(max_length=100)
    breed=models.CharField(max_length=100)
    age=models.IntegerField()
    health=models.CharField(max_length=100)
    price=models.IntegerField()
    owner_name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    c_number=models.IntegerField(default=0)
    image=models.ImageField(upload_to='media/pet_images')
    
    def __str__(self):
        return self.name 
    
class Petsitter(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.TextField()
    contact=models.IntegerField() 
    start_date=models.DateField(null=True,blank=True)
    end_date=models.DateField(null=True, blank=True)
    status=models.CharField(max_length=100,default='Available') 
    
    def __str__(self):
        return self.name
    
class Service(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField()
    number=models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
