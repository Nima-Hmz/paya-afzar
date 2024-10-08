# Generated by Django 5.0 on 2024-09-09 20:42

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_contactus_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Updating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True, verbose_name='فعال کردن وضعیت توسعه')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('description', tinymce.models.HTMLField(verbose_name='توضیحات')),
            ],
        ),
    ]
