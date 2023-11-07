# Generated by Django 4.2.5 on 2023-10-20 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customuser_is_email_verification'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userrole',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='userrole',
            name='group',
        ),
        migrations.RemoveField(
            model_name='userrole',
            name='user',
        ),
        migrations.DeleteModel(
            name='CustomGroup',
        ),
        migrations.DeleteModel(
            name='CustomPermission',
        ),
        migrations.DeleteModel(
            name='UserRole',
        ),
    ]