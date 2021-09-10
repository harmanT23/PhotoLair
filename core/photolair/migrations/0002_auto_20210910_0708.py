# Generated by Django 3.2.7 on 2021-09-10 07:08

from django.db import migrations, models
import photolair.image_handler
import profanity.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photolair', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(help_text='URL to image file', upload_to=photolair.image_handler.upload_image_path, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_name',
            field=models.CharField(help_text='Name of image specified by user.', max_length=100, validators=[profanity.validators.validate_is_profane], verbose_name='Image Name'),
        ),
    ]
