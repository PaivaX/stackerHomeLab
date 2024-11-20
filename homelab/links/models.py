from django.db import models

class Link(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição", blank=True)
    url = models.URLField(verbose_name="URL")
    open_in_new_tab = models.BooleanField(default=False, verbose_name="Abrir em nova janela")
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name="Imagem")
    active = models.BooleanField(default=True, verbose_name="Ativo")

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"
        ordering = ['name']

    def __str__(self):
        return self.name
