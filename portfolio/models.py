from django.db import models

class EmpresaParceira(models.Model):
    nome = models.CharField(max_length=200)
    area_atividade = models.CharField(max_length=200)
    descricao = models.TextField()
    website = models.URLField()
    logo = models.ImageField(upload_to='empresas/')

    def __str__(self):
        return self.nome

class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    grau = models.CharField(max_length=100)
    area_cientifica = models.CharField(max_length=150)
    duracao = models.IntegerField()
    ects = models.IntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='licenciaturas/')
    empresas_parceiras = models.ManyToManyField(
        EmpresaParceira,
        related_name='licenciaturas'
    )

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    pagina_pessoal = models.URLField()
    foto = models.ImageField(upload_to='docentes/')

    def __str__(self):
        return self.nome

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=200)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='ucs/')
    licenciatura = models.ForeignKey(
        Licenciatura, 
        on_delete=models.CASCADE,
        related_name='ucs'
    )
    docentes = models.ManyToManyField(
        Docente,
        related_name='ucs'
    )

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)
    descricao = models.TextField()
    logo = models.ImageField(upload_to='tecnologias/')
    link_oficial = models.URLField()
    nivel_preferencia = models.IntegerField()

    def __str__(self):
        return self.nome  

class Competencia(models.Model):
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return self.nome  

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    ano = models.IntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos/')
    conceitos_aplicados = models.TextField()
    github_link = models.URLField()
    video_demo = models.URLField(blank=True, null=True)
    unidade_curricular = models.ForeignKey(
        UnidadeCurricular,
        on_delete=models.CASCADE,
        related_name='projetos'
    )

    tecnologias = models.ManyToManyField(
        Tecnologia,
        related_name='projetos'
    )

    competencias = models.ManyToManyField(
        Competencia,
        related_name='projetos'
    )

    def __str__(self):
        return self.titulo
    
class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    orientador = models.CharField(max_length=200)
    curso = models.CharField(max_length=200)
    ano = models.IntegerField()
    resumo = models.TextField()
    classificacao = models.IntegerField()
    tecnologias = models.ManyToManyField(
        Tecnologia,
        related_name='tfcs'
    )

    def __str__(self):
        return self.titulo   

class Formacao(models.Model):
    nome = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    descricao = models.TextField()
    competencias = models.ManyToManyField(
        Competencia,
        related_name='formacoes'
    )

    def __str__(self):
        return self.nome

class MakingOf(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateField()
    imagem = models.ImageField(upload_to='makingof/', blank=True, null=True)
    decisao = models.TextField(blank=True, null=True)
    erro = models.TextField(blank=True, null=True)
    correcao = models.TextField(blank=True, null=True)
    justificacao = models.TextField(blank=True, null=True)
    uso_ia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo












    



# Create your models here.
