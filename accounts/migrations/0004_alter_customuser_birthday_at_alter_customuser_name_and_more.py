# Generated by Django 4.2.5 on 2023-10-06 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_birthday_at_alter_customuser_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birthday_at',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='surname',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
