# Generated by Django 4.2 on 2024-03-23 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_ipaddress_article_hits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='hits',
        ),
        migrations.DeleteModel(
            name='IPAddress',
        ),
    ]