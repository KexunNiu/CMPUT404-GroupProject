# Generated by Django 3.1.6 on 2022-10-26 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0005_auto_20221027_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='single_author',
            name='profileImage',
            field=models.ImageField(blank=True, upload_to='avatars/'),
        ),
    ]