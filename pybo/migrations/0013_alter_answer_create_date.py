# Generated by Django 4.2.7 on 2023-12-08 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0012_alter_answer_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='create_date',
            field=models.DateTimeField(),
        ),
    ]
