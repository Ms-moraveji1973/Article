# Generated by Django 4.2 on 2024-01-29 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_category_rename_is_active_article_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='articles'),
        ),
    ]
