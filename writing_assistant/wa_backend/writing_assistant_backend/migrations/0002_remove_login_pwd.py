# Generated by Django 4.0.1 on 2023-08-01 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writing_assistant_backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='pwd',
        ),
    ]