from django.db import models

class Contato(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email' ,max_length=100)
    assunto = models.CharField('Assunto' ,max_length=120)
    mensagem = models.CharField('Mensagem',max_length=300)
    
    def __str__(self):
        return self.nome