# Generated by Django 5.0 on 2024-09-03 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='en_description',
            new_name='endescription',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='en_title',
            new_name='entitle',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='en_title',
            new_name='entitle',
        ),
    ]
