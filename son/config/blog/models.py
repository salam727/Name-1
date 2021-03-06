from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter
# Create your models here.
class Category(models.Model):
        title=models.CharField(max_length=100, verbose_name ="عنوان دسته بندی")
        slug=models.SlugField(max_length=100,unique=True, verbose_name ="آدرس دسته بندی")
        status = models.BooleanField(default=True, verbose_name ="آیا نمایش داده شود ؟")
        position = models.IntegerField(verbose_name = "پوزیشن")

        class Meta:
            verbose_name = "دسته بندی"
            verbose_name_plural = "دسته بندی ها"
            ordering = ['position']

        def __str__(self):
            return self.title


class Article(models.Model):
    STATUS_CHOICES=(
        ('d', 'پیش نویس'),
        ('p', 'منتشر شده'),
    )
    title=models.CharField(max_length=100, verbose_name ="عنوان مقاله")
    slug=models.SlugField(max_length=100,unique=True, verbose_name ="آدرس مقاله")
    description = models.TextField(verbose_name ="متن")
    categoty=models.ManyToManyField(Category, verbose_name="دسته بندی")
    thumbnail = models.ImageField(upload_to="images", verbose_name ="تصویر")
    publish = models.DateTimeField(default=timezone.now, verbose_name ="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name ="وضعیت")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"


    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار"
