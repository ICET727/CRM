# Generated by Django 2.2.4 on 2019-09-11 08:59

import crm.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0020_lead_dob1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='attachment',
            field=models.FileField(upload_to='Cases/', validators=[crm.validators.validate_file_extension]),
        ),
    ]
