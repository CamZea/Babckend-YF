from django.db import models
from users.models import User

# Create your models here.
class Comunity(models.Model):
    name= models.CharField(max_length=100, null=False, blank=True)
    status= models.CharField(
         null= True,
         blank=True,
         choices=[
              ('created', 'Creado'),
              ('in_progress', 'En progreso'),
              ('finished', 'Terminado')
         ]
    )
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    class Meta:
        db_table= 'comunidades'

    def __str__(self) -> str:
            return self.name
        
class Foro(models.Model):
    name= models.CharField(max_length=255, null=False,blank=True )
    user= models.ForeignKey(
         User, on_delete=models.CASCADE, null= True, blank=True
    )
    post= models.TextField(null= True, blank= True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now= True)

    class Meta:
         db_table= 'foro'
