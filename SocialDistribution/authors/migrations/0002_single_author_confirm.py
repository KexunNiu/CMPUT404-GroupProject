# Generated by Django 3.1.6 on 2022-10-27 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='single_author',
            name='confirm',
            field=models.CharField(choices=[['true', 'TRUE'], ['false', 'FALSE']], default='False', max_length=6),
        ),
    ]
