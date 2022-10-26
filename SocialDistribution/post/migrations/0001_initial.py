# Generated by Django 3.1.6 on 2022-10-26 07:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment', models.TextField(blank=True, null=True)),
                ('published', models.DateTimeField(auto_now_add=True, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('type', models.CharField(default='post', max_length=200)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('content', models.CharField(blank=True, max_length=256, null=True)),
                ('Categories', models.TextField(blank=True, null=True)),
                ('published', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
