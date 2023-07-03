from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)
    email = models.EmailField(max_length=150)
    nome = models.CharField(max_length=150)
    apelido = models.CharField(max_length=150)
    Nif = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    cep = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    is_vendor = models.BooleanField(default=False)
    nome_empresa = models.CharField(max_length=150, blank=True, null=True)
    nif_empresa = models.CharField(max_length=20, blank=True, null=True)
    endereco_empresa = models.CharField(max_length=200, blank=True, null=True)
    cep_empresa = models.CharField(max_length=20, blank=True, null=True)
    telefone_empresa = models.CharField(max_length=20, blank=True, null=True)
    email_empresa = models.EmailField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.user.username

