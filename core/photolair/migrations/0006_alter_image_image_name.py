# Generated by Django 3.2.7 on 2021-09-20 07:29

from django.db import migrations, models
import profanity.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photolair', '0005_alter_user_credits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_name',
            field=models.CharField(help_text='Name of image specified by user. Max 100 characters.', max_length=100, validators=[profanity.validators.validate_is_profane], verbose_name='Image Name'),
        ),
    ]