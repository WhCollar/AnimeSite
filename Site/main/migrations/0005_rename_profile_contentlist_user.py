# Generated by Django 4.0.1 on 2022-02-10 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_contentlist_profile_alter_userprofiles_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contentlist',
            old_name='profile',
            new_name='user',
        ),
    ]