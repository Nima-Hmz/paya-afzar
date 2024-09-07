# Generated by Django 5.0 on 2024-09-02 12:42

import django.db.models.deletion
import django.utils.timezone
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
                ('en_name', models.CharField(max_length=200, verbose_name='نام انگلیسی')),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True, verbose_name='اسلاگ')),
                ('description', tinymce.models.HTMLField(blank=True, null=True, verbose_name='توضیحات دسته بندی اختیاری')),
                ('en_description', tinymce.models.HTMLField(blank=True, null=True, verbose_name='توضیحات دسته بندی انگلیسی اختیاری')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.category', verbose_name='دسته بندی مادر')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی\u200cها',
                'ordering': ('parent__id',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
                ('en_name', models.CharField(max_length=200, verbose_name='نام انگلیسی')),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True, verbose_name='آدرس')),
                ('image', models.ImageField(upload_to='products/', verbose_name='عکس')),
                ('description', tinymce.models.HTMLField(verbose_name='توضیحات و اطلاعات')),
                ('en_description', tinymce.models.HTMLField(verbose_name='توضیحات و اطلاعات انگلیسی')),
                ('available', models.BooleanField(default=True, verbose_name='وضعیت نمایش')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='به\u200cروز شده')),
                ('position', models.IntegerField(verbose_name='موقعیت در نمایش')),
                ('category', models.ManyToManyField(related_name='products', to='products.category', verbose_name='دسته\u200cبندی')),
                ('more_product', models.ManyToManyField(blank=True, to='products.product', verbose_name='محصولات مرتبط')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
                'ordering': ('-position',),
            },
        ),
    ]
