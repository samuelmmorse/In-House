# Generated by Django 4.0.1 on 2022-02-21 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_alter_user_picture"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="picture",
        ),
    ]
