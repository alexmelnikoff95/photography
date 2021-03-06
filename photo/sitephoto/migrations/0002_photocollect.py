# Generated by Django 4.0.1 on 2022-01-24 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitephoto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoCollect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(upload_to='movie_shots/')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitephoto.photo', verbose_name='фото')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
    ]
