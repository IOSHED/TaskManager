# Generated by Django 4.2.5 on 2023-10-23 15:26

import accounts.lib.path
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_customuser_icon_128_customuser_icon_32'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='icon_32',
            new_name='icon32',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='icon_128',
        ),
        migrations.AddField(
            model_name='customuser',
            name='icon64',
            field=models.ImageField(
                default='default/user_icon_64.png', upload_to=accounts.lib.path.user_directory_path),
        ),
    ]
