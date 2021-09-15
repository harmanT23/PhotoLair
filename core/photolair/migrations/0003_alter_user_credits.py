# Generated by Django 3.2.7 on 2021-09-11 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photolair', '0002_auto_20210910_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='credits',
            field=models.PositiveBigIntegerField(blank=True, default=10, help_text='Account balance of credits available to the user', verbose_name='Credits'),
        ),
    ]