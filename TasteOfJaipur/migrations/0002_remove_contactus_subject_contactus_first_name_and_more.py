# Generated by Django 4.1.7 on 2023-03-01 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TasteOfJaipur", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contactus",
            name="subject",
        ),
        migrations.AddField(
            model_name="contactus",
            name="first_name",
            field=models.CharField(default="shubham", max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="contactus",
            name="email",
            field=models.EmailField(max_length=150),
        ),
        migrations.AlterField(
            model_name="contactus",
            name="message",
            field=models.CharField(max_length=2000),
        ),
    ]
