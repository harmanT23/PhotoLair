# Generated by Django 3.2.7 on 2021-09-11 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photolair', '0003_alter_user_credits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='inventory',
            field=models.PositiveBigIntegerField(default=0, help_text='Defines number of available image downloads.', verbose_name='inventory'),
        ),
    ]
