# Generated by Django 4.2.11 on 2024-04-03 09:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customuser",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "User",
                "verbose_name_plural": "Users",
            },
        ),
    ]
