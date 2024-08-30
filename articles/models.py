from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    """
    Category model that holds some sorts of categories that used in the blog
    """

    title = models.CharField(max_length=200, verbose_name=("عنوان دسته‌بندی"))
    en_title = models.CharField(max_length=200, verbose_name=("عنوان دسته‌بندی انگلیسی"))
    slug = models.SlugField(max_length=100, unique=True, verbose_name=("آدرس دسته‌بندی"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("دسته‌بندی")
        verbose_name_plural = ("دسته‌بندی ها")
        ordering = ['title']


class Article(models.Model):
    """
    Article model that holds information about articles published on the blog.
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=("دسته بندی"), help_text=("دسته بندی پست خود را وارد کنید"), related_name="blog")
    title = models.CharField(max_length=200, verbose_name=("عنوان مقاله"), help_text=("عنوان مقاله را وارد کنید"))
    en_title = models.CharField(max_length=200, verbose_name=("عنوان مقاله انگلیسی"), help_text=("عنوان مقاله را وارد کنید انگلیسی"))
    slug = models.SlugField(max_length=100, verbose_name=("آدرس مقاله"), help_text=("آدرس مقاله را میتوانید از اینجا عوض کنید،(نکته: فقط در زمان ویرایش مقاله امکان تغییر آدرس وجود دارد) اما با عوض کردن آن آدرس قبلی در دسترس نخواهد بود"))
    description = RichTextField(verbose_name=("مقاله"), help_text=("محتوای مقاله را وارد کنید"))
    en_description = RichTextField(verbose_name=("مقاله انگلیسی"), help_text=("محتوای مقاله را وارد کنید انگلیسی"))
    thumbnail = models.ImageField(upload_to='images/blog/%Y/%m/%d', verbose_name=("تصویر مقاله"), help_text=("تصویری که میخواهید به عنوان کاور مقاله قرار بگیرد را وارد کنید"))
    pub_date = models.DateTimeField(default=timezone.now, verbose_name=("زمان انتشار"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True, verbose_name=("وضعیت انتشار"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("مقاله")
        verbose_name_plural = ("مقالات")
        ordering = ['-pub_date']





