from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = RichTextField(verbose_name="Содержание")
    image = models.ImageField(upload_to='blog/images/', verbose_name="Картинка")
    tags = models.ManyToManyField('Tag', verbose_name="Теги")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Категория")
    slug = models.SlugField(unique=True, verbose_name="Слаг")

    publication_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название тега")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    

@receiver(post_delete, sender=BlogPost)
def delete_post_image(sender, instance, **kwargs):
    # Удаление картинки поста при удалении поста
    if instance.image:
        image_path = instance.image.path
        if default_storage.exists(image_path):
            default_storage.delete(image_path)