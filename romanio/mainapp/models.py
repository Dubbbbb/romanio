from django.db import models
from django.urls import reverse


class Product(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey("SubCategory", verbose_name="Категория", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name="Изображение")
    description = models.TextField(verbose_name="Описание", null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")


    def __str__(self):
        return self.title

class Door(Product):

    class Meta():
        verbose_name = 'Дверь'
        verbose_name_plural = 'Двери'

class Window(Product):

    class Meta():
        verbose_name = 'Окно'
        verbose_name_plural = 'Окна'


class SubCategory(models.Model):
    title = models.CharField(max_length=50, verbose_name="Категория")
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug_url": self.slug})
    

    class Meta():
        verbose_name = 'Категории'
        verbose_name_plural = 'Категория'


# class SecondCategory(models.Model):
#     title = models.CharField(max_length=50, verbose_name="Подкатегория")
#     slug = models.SlugField(max_length=50, unique=True)
#     maincategory = models.ForeignKey(MainCategory,verbose_name="Основная категория", on_delete=models.CASCADE )

#     def __str__(self):
#         return self.title

#     class Meta():
#         verbose_name = 'Подкатегория'
#         verbose_name_plural = 'Подкатегории'


