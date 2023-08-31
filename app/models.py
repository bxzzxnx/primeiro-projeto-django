from django.db import models

# Create your models here.


class User(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=144, null=False)

    def __str__(self):
        return self.nome
