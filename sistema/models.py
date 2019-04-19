from django.db import models
from datetime import date

# Create your models here.

# Model do Acolhido da instituicao
class Acolhido(models.Model):
    nome = models.CharField(max_length=40, blank=True)
    data_nasc = models.DateField(default=date.today)
    data_entrada = models.DateField(default=date.today)
    cid_natal = models.CharField(max_length=50, blank=True)
    uf = models.CharField(max_length=2, default="SP", blank=True)
    imagem = models.ImageField(upload_to='img_acolhidos', default='media/default.png', blank=True)
    nome_mae = models.CharField(max_length=40, default="", blank=True)
    resp_mae = models.BooleanField(default=False, blank=True)
    nome_pai = models.CharField(max_length=40, default="", blank=True)
    resp_pai = models.BooleanField(default=False, blank=True)
    nome_resp = models.CharField(max_length=40, default="", blank=True)
    resp_resp = models.BooleanField(default=False, blank=True)
    cpf = models.CharField(max_length=11, blank=True)
    rg = models.CharField(max_length=11, blank=True)
    ssp = models.CharField(max_length=2, blank=True)
    renda = models.DecimalField(max_digits=6, decimal_places=2, default=0, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True)
    camiseta = models.CharField(max_length=2, blank=True)
    calca = models.CharField(max_length=2, blank=True)
    intima = models.CharField(max_length=1, blank=True)
    calcado = models.CharField(max_length=2, blank=True)
    alergias = models.TextField(blank=True)
    sangue = models.CharField(max_length=1, blank=True)
    qtd_aborto = models.IntegerField(blank=True, null=True)

    def __str__(self):  # Equivalente ao .toString do Java
        return self.nome

class Residencia(models.Model):
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=65)
    numero = models.CharField(max_length=4)
    complemento = models.CharField(max_length=15)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)

class Trabalho(models.Model):
    empresa = models.CharField(max_length=30)
    cargo = models.CharField(max_length=20)
    salario = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=65)
    numero = models.CharField(max_length=4)
    complemento = models.CharField(max_length=15)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)

class Juridico(models.Model):
    processo = models.CharField(max_length=25)
    comarca = models.CharField(max_length=30)
    nro_vara = models.CharField(max_length=2)
    vara = models.CharField(max_length=20)

class Doador(models.Model):
    nome = models.CharField(max_length=40)
    data_entrada = models.DateField(default=date.today)
    email = models.EmailField(max_length=30)
    #imagem = models.ImageField(upload_to='img_doadores', default='media/default.png')
    tel_residencial = models.CharField(max_length=10)
    tel_celular = models.CharField(max_length=10)
    tel_comercial = models.CharField(max_length=10)
    voluntario = models.BooleanField(default=False)
    financeiro = models.BooleanField(default=False)
    vestuario = models.BooleanField(default=False)
    alimenticio = models.BooleanField(default=False)

class Movimentacao(models.Model):
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    CHOICES = (
                ('ENTRADA', 'Entrada'),
                ('SAIDA', 'Saída'),
                ('DOACAO', 'Doação'),
              )
    tipo = models.CharField(choices=CHOICES, max_length=7)
    descricao = models.CharField(max_length=150)
    data = models.DateField(default=date.today)
    qtd = models.IntegerField()

class Produto(models.Model):
    descricao = models.CharField(max_length=150)
    qtd = models.IntegerField()
    unidade = models.CharField(max_length=20)
    data_validade = models.DateField(default=date.today)
    preco_entrada = models.DecimalField(max_digits=7, decimal_places=2)
    
class Doacao(models.Model):
    descricao = models.CharField(max_length=150)
    tipo_doacao = models.CharField(max_length=10)   # Bens, Dinheiro e Tempo
    #doador
    qtd = models.IntegerField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    # Doador

class Caixa(models.Model):
    vlr_disponivel = models.DecimalField(max_digits=7, decimal_places=2)
    # Set de Movimentacao

class Configuracao(models.Model):
    novo_nome = models.CharField(max_length=20)

# Classe de Usuario
