# Generated by Django 4.0.2 on 2022-03-06 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("boardmanlab", "0006_alter_helpsession_is_online"),
    ]

    operations = [
        migrations.RenameField(
            model_name="helpsession",
            old_name="is_online",
            new_name="is_remote",
        ),
    ]
