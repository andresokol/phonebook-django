# Generated by Django 2.2.19 on 2022-07-08 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todotask",
            name="is_done",
            field=models.BooleanField(default=False),
        ),
    ]