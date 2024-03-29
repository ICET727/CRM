# Generated by Django 2.2.4 on 2019-09-10 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0017_auto_20190909_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
