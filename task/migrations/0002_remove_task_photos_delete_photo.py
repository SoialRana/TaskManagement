# Generated by Django 4.2.6 on 2023-11-02 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='photos',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]