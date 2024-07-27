from django.db import models

# Create your models here.

class User(models.Model):
    name= models.CharField(max_length=255)
    lastname=models.CharField(max_length=255, null= True, blank=True)
    email= models.EmailField(unique=True)
    password= models.CharField(max_length=200)
    is_super_user= models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    class Meta:
        db_table= 'users'
     
    

