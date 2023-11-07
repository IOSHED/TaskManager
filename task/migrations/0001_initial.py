# Generated by Django 4.2.5 on 2023-10-20 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255, null=True)),
                ('description', models.TextField(max_length=510, null=True)),
                ('send_notify_at', models.DateTimeField()),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('complete_at', models.DateField(null=True)),
                ('is_complete', models.BooleanField(default=False)),
            ],
        ),
    ]