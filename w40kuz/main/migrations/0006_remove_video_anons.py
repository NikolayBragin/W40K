# Generated by Django 5.0.2 on 2024-03-11 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_articles_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='anons',
        ),
    ]
