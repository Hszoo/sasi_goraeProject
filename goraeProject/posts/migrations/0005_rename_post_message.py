# Generated by Django 4.2.3 on 2023-07-28 09:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_alter_userinfo_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Message',
        ),
    ]
