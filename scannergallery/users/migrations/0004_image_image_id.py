# Generated by Django 3.1.1 on 2024-04-11 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20240402_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_id',
            field=models.CharField(default='1800suck me', help_text='Image link here', max_length=500),
        ),
    ]
