# Generated by Django 3.2.8 on 2021-10-14 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Obras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('editora', models.CharField(max_length=250)),
                ('foto', models.URLField()),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('autores', models.ManyToManyField(to='obras.Autor')),
            ],
            options={
                'ordering': ['data_criacao'],
            },
        ),
    ]