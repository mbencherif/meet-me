# Generated by Django 2.1.7 on 2019-05-05 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatMe', '0002_auto_20190505_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='missed_call',
            field=models.BooleanField(default=False),
        ),
    ]