# Generated by Django 4.1.1 on 2022-09-17 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserModel",
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
                ("name", models.CharField(max_length=30)),
                ("login", models.CharField(max_length=30)),
                ("password", models.CharField(max_length=16)),
                ("role_admin", models.BooleanField()),
                ("role_owner", models.BooleanField()),
            ],
            options={"verbose_name": "user", "verbose_name_plural": "users", },
        ),
    ]
