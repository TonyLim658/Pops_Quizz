# Generated by Django 3.0.6 on 2020-05-19 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quizz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PossibleAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.TextField()),
                ('correct', models.BooleanField(default=False)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.TextField()),
                ('order', models.IntegerField()),
                ('answerType', models.CharField(max_length=255)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quizz.Form')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255, unique=True)),
                ('mail', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AddField(
            model_name='possibleanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quizz.Question'),
        ),
        migrations.AddField(
            model_name='form',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Quizz.User'),
        ),
    ]