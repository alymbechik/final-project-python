# Generated by Django 5.1 on 2024-08-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_lead'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='subject',
            field=models.CharField(default=1, max_length=123),
            preserve_default=False,
        ),
    ]
