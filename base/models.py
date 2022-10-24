from django.db import models

# Create your models here.

class Base(models.Model):
    creation = models.DateField("Data de criação", auto_now_add=True)
    modified = models.DateField("Data de atualização", auto_now= True)
    active = models.BooleanField("Ativo?", default= True)
    
    class Meta:
        abstract = True

class User(Base):
    email = models.EmailField("E-mail", max_length=100)
    password = models.CharField("Senha", max_length=20)
    
    def __str__(self):
        return self.email
