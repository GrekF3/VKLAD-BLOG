# Generated by Django 4.2.5 on 2023-09-16 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_main_image_blogpost_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(default='CategoriesImages/empty.jpg', help_text='540x540', upload_to='CategoriesImages/', verbose_name='Картинка категории'),
        ),
    ]
