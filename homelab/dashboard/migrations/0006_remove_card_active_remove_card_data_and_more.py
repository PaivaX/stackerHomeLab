# Generated by Django 5.1.3 on 2024-11-19 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_card_open_in_new_tab'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='active',
        ),
        migrations.RemoveField(
            model_name='card',
            name='data',
        ),
        migrations.RemoveField(
            model_name='card',
            name='last_updated',
        ),
        migrations.RemoveField(
            model_name='card',
            name='update_frequency',
        ),
        migrations.AddField(
            model_name='card',
            name='api_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='html_code',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='refresh_interval',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='card',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_type',
            field=models.CharField(choices=[('link', 'Link'), ('html', 'HTML'), ('api', 'API'), ('custom', 'Custom')], max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]