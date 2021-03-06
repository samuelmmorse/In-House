# Generated by Django 4.0.2 on 2022-02-22 22:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0012_alter_user_username"),
    ]

    operations = [
        migrations.CreateModel(
            name="Topic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("topic", models.TextField(blank=True, max_length=300, null=True)),
                ("user", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "ordering": ["topic"],
            },
        ),
    ]
