# Generated by Django 3.0 on 2023-05-03 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20230503_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='home',
            field=models.BooleanField(default=False),
        ),
    ]