# Generated by Django 2.2.19 on 2021-04-21 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210421_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.FloatField(),
        ),
    ]
