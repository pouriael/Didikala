# Generated by Django 4.0.4 on 2022-07-13 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0007_alter_formprofile_profile_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formprofile',
            options={'verbose_name': 'پروفایل', 'verbose_name_plural': 'پروفایل ها '},
        ),
        migrations.AlterField(
            model_name='formprofile',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='formprofile',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31, null=True, verbose_name='شماره همراه'),
        ),
        migrations.AlterField(
            model_name='formprofile',
            name='profile_image',
            field=models.ImageField(blank=True, default='dress.jfif', null=True, upload_to='profile/', verbose_name='عکس پروفایل'),
        ),
        migrations.AlterField(
            model_name='formprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
