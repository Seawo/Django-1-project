# Generated by Django 4.2.7 on 2023-12-04 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0002_rename_creat_date_answer_create_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='create_date',
            new_name='create_dat',
        ),
    ]