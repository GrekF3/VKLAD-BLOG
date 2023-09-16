from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils.html import strip_tags
import re
from PIL import Image



class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = RichTextField(verbose_name="Содержание")
    image = models.ImageField(upload_to='blog/images/', verbose_name="Картинка")
    tags = models.ManyToManyField('Tag', verbose_name="Теги")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Категория")
    slug = models.SlugField(unique=True, verbose_name="Слаг")

    publication_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    reading_time_minutes = models.IntegerField(verbose_name="Время чтения (минуты)", null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.image.path)
        new_size = (600, 600)
        image.thumbnail(new_size)
        image.save(self.image.path)

        if not self.id:
            # Рассчитываем время чтения только при создании нового поста
            post_content = strip_tags(self.content)
            words = re.findall(r'\w+', post_content)
            word_count = len(words)
            average_reading_speed = 225  # Пример средней скорости чтения (слов в минуту)
            reading_time_minutes = word_count / average_reading_speed
            self.reading_time_minutes = int(reading_time_minutes)



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
    category_image = models.ImageField(upload_to='CategoriesImages/', verbose_name='Картинка категории', help_text='540x540')

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