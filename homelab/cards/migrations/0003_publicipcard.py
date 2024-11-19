# Generated by Django 5.1.3 on 2024-11-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_card_delete_publicipcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicIPCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('card_type', models.CharField(default='public_ip', max_length=50)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('data', models.JSONField(default=dict)),
            ],
        ),
    ]
