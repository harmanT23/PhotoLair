# Generated by Django 3.2.7 on 2021-09-10 06:40

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from photolair.utilities import upload_image_path
import photolair.managers
import profanity.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='User ID is a uuid.', primary_key=True, serialize=False, verbose_name='ID')),
                ('credits', models.PositiveBigIntegerField(blank=True, default=10, help_text='Default number of credits each user starts with', verbose_name='Credits')),
                ('created_at', models.DateTimeField(auto_now=True, help_text='Indicates when user instance was created.', verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Indicates when user instance was last updated.', verbose_name='Updated At')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', photolair.managers.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Image ID is a uuid.', primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(help_text='Name of image.', max_length=100, validators=[profanity.validators.validate_is_profane], verbose_name='Image Name')),
                ('image', models.ImageField(help_text='URL to image file/', upload_to=upload_image_path, verbose_name='Image')),
                ('inventory', models.PositiveBigIntegerField(default=0, help_text='Defines number of available image downloads.', verbose_name='Credits')),
                ('price', models.PositiveBigIntegerField(default=0, help_text='Defines price (in credits) for each image download.', verbose_name='Price')),
                ('created_at', models.DateTimeField(auto_now=True, help_text='Indicates when image instance was created.', verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Indicates when image instance was last updated.', verbose_name='Updated At')),
                ('user', models.ForeignKey(help_text='Image belongs to associated User.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]
