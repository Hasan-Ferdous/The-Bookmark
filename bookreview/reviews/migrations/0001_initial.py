# Generated by Django 5.1.6 on 2025-02-06 06:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('published_date', models.DateField()),
                ('genre', models.CharField(max_length=100)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='book_covers/')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('review_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.book')),
            ],
        ),
    ]
