# Generated by Django 3.0.6 on 2021-02-28 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posthog", "0129_merge_20210223_0757"),
    ]

    operations = [
        migrations.AddField(
            model_name="dashboard",
            name="creation_mode",
            field=models.CharField(
                choices=[("default", "Default"), ("template", "Template"), ("duplicate", "Duplicate")],
                default="default",
                max_length=16,
            ),
        ),
    ]