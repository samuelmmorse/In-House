# Generated by Django 4.0.1 on 2022-02-21 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0008_remove_user_picture"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="picture",
            field=models.CharField(default="", max_length=200),
        ),
    ]
