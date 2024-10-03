# Generated by Django 5.1 on 2024-09-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('salary', models.PositiveIntegerField()),
                ('contact', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
