# Generated by Django 4.2 on 2024-03-08 12:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_special_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=' کاربر ویژه تا'),
        ),
    ]
