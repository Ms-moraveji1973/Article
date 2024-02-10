# Generated by Django 4.2 on 2024-02-01 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_alter_article_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='article.category', verbose_name='Children'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='articles_cat', to='article.category', verbose_name='دسته بندی مقاله'),
        ),
    ]