from django.db import models

class Todo(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    criar_atividade = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    prazo_final = models.DateTimeField(null=False, blank=False)
    finalziar_atividade = models.DateTimeField(null=True)


