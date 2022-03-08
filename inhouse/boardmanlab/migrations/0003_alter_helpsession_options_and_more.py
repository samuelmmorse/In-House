# Generated by Django 4.0.1 on 2022-03-01 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boardmanlab", "0002_helpsession_time"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="helpsession",
            options={"ordering": ["time"]},
        ),
        migrations.AlterField(
            model_name="helpsession",
            name="attendance",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
