# Generated by Django 5.0.7 on 2024-11-09 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0003_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='photo/category')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
