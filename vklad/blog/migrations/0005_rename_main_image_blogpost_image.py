# Generated by Django 4.2.5 on 2023-09-16 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_image_blogpost_main_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='main_image',
            new_name='image',
        ),
    ]
