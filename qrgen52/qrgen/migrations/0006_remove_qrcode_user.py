# Generated by Django 4.1 on 2022-08-10 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qrgen', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qrcode',
            name='user',
        ),
    ]