from django.db import models

class Product(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.nome
