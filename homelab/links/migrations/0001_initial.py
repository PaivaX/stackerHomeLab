# Generated by Django 5.1.3 on 2024-11-20 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('url', models.URLField(verbose_name='URL')),
                ('open_in_new_tab', models.BooleanField(default=False, verbose_name='Abrir em nova janela')),
                ('image', models.ImageField(blank=True, null=True, upload_to='link_images/', verbose_name='Imagem')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
                'ordering': ['name'],
            },
        ),
    ]
