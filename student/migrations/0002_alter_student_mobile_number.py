# Generated by Django 4.2.17 on 2024-12-17 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mobile_number',
            field=models.BigIntegerField(),
        ),
    ]