# Generated by Django 4.2.6 on 2023-10-30 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('Imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),
                ('Sipnosis', models.TextField(verbose_name='Sipnosis')),
            ],
        ),
    ]
