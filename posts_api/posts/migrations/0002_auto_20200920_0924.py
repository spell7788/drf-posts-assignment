# Generated by Django 3.1.1 on 2020-09-20 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upvotes_number',
            field=models.PositiveSmallIntegerField(default=0, help_text='The number of post upvotes.', verbose_name='upvotes number'),
        ),
    ]
