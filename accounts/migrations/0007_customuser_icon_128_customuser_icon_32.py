# Generated by Django 4.2.5 on 2023-10-21 15:10

import accounts.lib.path
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_userrole_unique_together_remove_userrole_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='icon_128',
            field=models.ImageField(
                default='default/user_icon_128.png', upload_to=accounts.lib.path.user_directory_path),
        ),
        migrations.AddField(
            model_name='customuser',
            name='icon_32',
            field=models.ImageField(
                default='default/user_icon_32.png', upload_to=accounts.lib.path.user_directory_path),
        ),
    ]