# Generated by Django 4.1.1 on 2022-09-18 16:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0001_initial"),
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="usermodel",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="company.companymodel",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="usermodel",
            name="role_admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="usermodel",
            name="role_owner",
            field=models.BooleanField(default=False),
        ),
    ]
