# Generated by Django 4.0.3 on 2022-04-05 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_position_alter_user_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.position'),
        ),
    ]
