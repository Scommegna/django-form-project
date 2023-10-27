from django.db import models
from stdimage import StdImageField

from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)
    
    class Meta:
        abstract = True

class Contato(Base):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email' ,max_length=100)
    assunto = models.CharField('Assunto' ,max_length=120)
    mensagem = models.CharField('Mensagem',max_length=300)
    
    def __str__(self):
        return self.nome
    
class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124,124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
    
    def __str__(self):
        return self.nome
    
def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)
    
signals.pre_save.connect(produto_pre_save, sender=Produto)