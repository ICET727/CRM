# Generated by Django 2.2.4 on 2019-09-07 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_auto_20190907_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='performa',
            name='insurance',
            field=models.BooleanField(default=False),
        ),
    ]