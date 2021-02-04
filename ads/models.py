from django.db import migrations, models

# Create your models here.

class Ads(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название товара')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    photo = models.ImageField(upload_to='images/', blank=True, verbose_name='Фотография')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name="Категория")

    class Meta:
        verbose_name_plural = 'Обьявления'
        verbose_name = 'Обьявление'
        ordering = ['-published']


class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']
