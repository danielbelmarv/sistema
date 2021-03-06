# Generated by Django 4.0.5 on 2022-06-25 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('imagen', models.ImageField(null=True, upload_to='img/', verbose_name='Imagen')),
                ('description', models.TextField(null=True, verbose_name='Descripcion')),
            ],
        ),
    ]
