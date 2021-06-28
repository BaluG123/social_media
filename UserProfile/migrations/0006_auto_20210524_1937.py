# Generated by Django 3.2.3 on 2021-05-24 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("UserProfile", "0005_customuser_email_verified"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="email_verified",
        ),
        migrations.AlterField(
            model_name="customuser",
            name="is_staff",
            field=models.BooleanField(default=True),
        ),
    ]
