# Generated by Django 4.0.4 on 2022-07-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_formprofile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formprofile',
            name='address',
            field=models.CharField(blank=True, default='glass_2.jpg', max_length=50, null=True),
        ),
    ]
