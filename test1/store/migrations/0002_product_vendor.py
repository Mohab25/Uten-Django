# Generated by Django 3.1 on 2020-11-18 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.CharField(default='', max_length=100),
        ),
    ]