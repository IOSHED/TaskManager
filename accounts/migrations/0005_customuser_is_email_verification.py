# Generated by Django 4.2.5 on 2023-10-14 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_birthday_at_alter_customuser_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_email_verification',
            field=models.BooleanField(default=False),
        ),
    ]
