from django.db import models
from django.contrib.auth.models import User

class Estado(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Leiloeiro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    site = models.URLField()

    def __str__(self):
        return self.nome

class Matricula(models.Model):
    leiloeiro = models.ForeignKey(Leiloeiro, on_delete=models.CASCADE, related_name='matriculas')
    numero = models.CharField(max_length=20)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.numero} - {self.estado.nome}"

class Anexo(models.Model):
    leiloeiro = models.ForeignKey(Leiloeiro, on_delete=models.CASCADE, related_name='anexos')
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE, related_name='anexos')
    arquivo = models.FileField(upload_to='anexos/')

    def __str__(self):
        return f"Anexo de {self.leiloeiro.nome}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
