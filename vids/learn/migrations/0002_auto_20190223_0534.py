# Generated by Django 2.1.7 on 2019-02-23 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threaddiscussion',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
