# Generated by Django 2.2.4 on 2019-09-10 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0018_auto_20190910_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='brief',
            name='criteria',
            field=models.CharField(blank=True, choices=[('Nature Identical', 'Nature Identical'), ('Natural', 'Natural'), ('Artificial', 'Artificial')], max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='brief',
            name='form',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='brief',
            name='mesh',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='brief',
            name='project_priority',
            field=models.CharField(blank=True, choices=[('Normal', 'Normal'), ('Fast', 'Fast'), ('Urgent', 'Urgent')], max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='brief',
            name='solubility',
            field=models.CharField(blank=True, choices=[('Oil', 'Oil'), ('Water', 'Water')], max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='brief',
            name='tentative_consumption',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_1kg',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_1kg10',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_1kg2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_1kg3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_1kg4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_1kg5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_1kg6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_1kg7',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_1kg8',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_1kg9',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_25kg',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_25kg10',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_25kg2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_25kg3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_25kg4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_25kg5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_25kg6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_25kg7',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_25kg8',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_25kg9',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_50kg',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_50kg10',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_50kg2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_50kg3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_50kg4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_50kg5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_50kg6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_50kg7',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_50kg8',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_50kg9',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_5kg',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_5kg10',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_5kg2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_5kg3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_5kg4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_5kg5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_5kg6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_5kg7',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_5kg8',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='price_per_5kg9',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
