# Generated by Django 3.1.4 on 2021-02-02 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название товара')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Цена')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m,%d/', verbose_name='Фотография')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ads.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Обьявление',
                'verbose_name_plural': 'Обьявления',
            },
        ),
    ]
