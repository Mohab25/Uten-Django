# Generated by Django 3.1 on 2020-10-19 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('call_to_action', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FirstBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('subtitle', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('btn_text', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='')),
                ('logo_description', models.TextField()),
                ('contact_info_title', models.TextField()),
                ('contact_info_location', models.TextField()),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('subtitle', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SecondBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_to_action_head', models.TextField()),
                ('call_to_action_message', models.TextField()),
                ('btn_message', models.CharField(max_length=100)),
            ],
        ),
    ]
