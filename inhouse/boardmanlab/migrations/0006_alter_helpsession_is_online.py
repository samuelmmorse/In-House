# Generated by Django 4.0.2 on 2022-03-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boardmanlab", "0005_helpsession_remote_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="helpsession",
            name="is_online",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
