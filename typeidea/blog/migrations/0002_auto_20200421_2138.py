# Generated by Django 3.0.5 on 2020-04-21 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='create_time',
            new_name='created_time',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='create_time',
            new_name='created_time',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='create_time',
            new_name='created_time',
        ),
    ]
