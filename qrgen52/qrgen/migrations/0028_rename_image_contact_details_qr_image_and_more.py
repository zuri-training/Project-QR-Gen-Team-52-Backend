# Generated by Django 4.1 on 2022-08-14 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qrgen', '0027_rename_image_create_link_qr_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_details',
            old_name='image',
            new_name='qr_image',
        ),
        migrations.RenameField(
            model_name='send_mail',
            old_name='image',
            new_name='qr_image',
        ),
        migrations.RenameField(
            model_name='text_message',
            old_name='image',
            new_name='qr_image',
        ),
    ]
