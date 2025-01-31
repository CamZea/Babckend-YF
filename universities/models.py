from django.db import models
# Create your models here.
class Carrier(models.Model):
    name = models.CharField(max_length=255,null=True)
    area = models.CharField(max_length=255,null=True)
    description = models.TextField(null= True,blank = True)
    image = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'carriers'
    
    