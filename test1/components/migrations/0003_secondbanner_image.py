# Generated by Django 3.1 on 2020-10-21 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0002_galleryitem_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondbanner',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]