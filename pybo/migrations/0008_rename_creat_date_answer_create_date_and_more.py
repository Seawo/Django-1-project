# Generated by Django 4.2.7 on 2023-12-07 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0007_question_author'),
    ]

    operations = [
        # migrations.RenameField(
        #     model_name='answer',
        #     old_name='creat_date',
        #     new_name='create_date',
        # ),
        migrations.AddField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
