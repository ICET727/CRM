# Generated by Django 2.2.4 on 2019-09-11 07:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0019_auto_20190910_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='dob1',
            field=models.DateField(default=datetime.datetime(2019, 9, 11, 7, 40, 47, 48700, tzinfo=utc)),
            preserve_default=False,
        ),
    ]