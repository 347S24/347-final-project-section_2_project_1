# Generated by Django 3.1.1 on 2024-04-23 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20240423_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.ImageField(null=True, upload_to='image_uploads'),
        ),
    ]
