# Generated by Django 4.0.4 on 2023-07-11 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0002_homepage_img_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='mypage/images'),
        ),
    ]
