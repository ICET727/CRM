# Generated by Django 2.2.4 on 2019-09-15 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0024_auto_20190913_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='categories',
        ),
        migrations.AddField(
            model_name='sample',
            name='item_quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sample',
            name='item_quantity10',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='item_quantity2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='item_quantity3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='item_quantity4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='item_quantity5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='item_quantity6',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='item_quantity7',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='item_quantity8',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='item_quantity9',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]