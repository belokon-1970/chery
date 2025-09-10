from django.db import models

class Artiles(models.Model):
    title = models.CharField('Название', max_length=50)
    image = models.ImageField(verbose_name="Картинка", null=True, blank=True)
    annons = models.CharField('Цена', max_length=250)
    full_text = models.TextField('Модель')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Новости'
