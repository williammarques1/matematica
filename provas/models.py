from django.db import models


class Tema(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Pergunta(models.Model):
    enunciado = models.CharField(max_length=200)
    dificuldade = models.CharField(max_length=20, default=None)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'perguntas'

    def __str__(self):
        return self.enunciado


class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto = models.TextField()
    data_publicacao = models.DateTimeField('data de publicação')
    correta = models.BooleanField(default=False)


class Questionario(models.Model):
    nome = models.CharField(max_length=100)
    perguntas = models.ManyToManyField(Pergunta)

    def __str__(self):
        return self.nome
    

class Aluno(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class QuestionarioRespondido(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)
    respostas = models.ManyToManyField(Resposta)

    def __str__(self):
        return f'{self.aluno.nome} - {self.questionario.nome}'