# Generated by Django 5.0 on 2024-09-04 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_endescription_aboutus_en_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='firsttitle',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='first_title/', verbose_name='تصویر 2'),
        ),
    ]
