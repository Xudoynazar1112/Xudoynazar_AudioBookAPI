# Generated by Django 5.1.2 on 2024-10-10 13:29

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_number', models.PositiveIntegerField(help_text="Total number of pages in the ebook (must be between 1 and the book's total pages)", validators=[django.core.validators.MinValueValidator(1)])),
                ('content', models.TextField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='book.book')),
            ],
            options={
                'ordering': ['page_number'],
                'unique_together': {('book', 'page_number')},
            },
        ),
    ]
