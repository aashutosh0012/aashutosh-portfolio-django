# Generated by Django 3.0.8 on 2021-05-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='label',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]