# Generated by Django 5.0.1 on 2024-10-01 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0014_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Youtube_thum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_name', models.CharField(max_length=120)),
            ],
        ),
    ]
