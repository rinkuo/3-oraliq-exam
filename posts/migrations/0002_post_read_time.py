# Generated by Django 5.1.5 on 2025-01-25 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='read_time',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
