# Generated by Django 5.1.3 on 2024-11-19 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_remove_card_created_at_remove_card_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='open_in_new_tab',
            field=models.BooleanField(default=False, help_text='Abrir o link em uma nova aba?'),
        ),
    ]
