from django.db import models

class Artiles(models.Model):
    title = models.CharField('Название', max_length=50)
    annons = models.CharField('Анонс', max_length=250)
    image = models.ImageField(verbose_name="Картинка", null=True, blank=True)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Новости'
