# Generated by Django 3.0.6 on 2020-06-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizz', '0020_auto_20200610_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='is_older_version',
            field=models.BooleanField(default=False),
        ),
    ]
