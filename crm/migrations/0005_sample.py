# Generated by Django 2.2.4 on 2019-09-07 05:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0004_auto_20190906_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item_quantity', models.IntegerField(blank=True, null=True)),
                ('stage', models.CharField(choices=[('APPROVAL', 'APPROVAL'), ('APPROVED', 'APPROVED'), ('SENT FOR PRODUCTION', 'SENT FOR PRODUCTION'), ('DISPATCHED', 'DISPATCHED'), ('DELIVERED', 'DELIVERED'), ('REJECTED', 'REJECTED')], default='APPROVAL', max_length=64)),
                ('packaging', models.CharField(default='BULK', max_length=100)),
                ('categories', models.CharField(max_length=100)),
                ('gst_number', models.CharField(max_length=30, unique=True)),
                ('statutory', models.CharField(blank=True, max_length=30, null=True)),
                ('per_item_price', models.IntegerField()),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('street', models.CharField(blank=True, max_length=30, null=True)),
                ('solubility', models.CharField(blank=True, choices=[('Oil Soluble', 'Oil Soluble'), ('Water Soluble', 'Water Soluble')], max_length=100, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=50)),
                ('ship_country', models.CharField(choices=[('GB', 'United Kingdom'), ('AF', 'Afghanistan'), ('AX', 'Aland Islands'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('AS', 'American Samoa'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarctica'), ('AG', 'Antigua and Barbuda'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BB', 'Barbados'), ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BT', 'Bhutan'), ('BO', 'Bolivia'), ('BA', 'Bosnia and Herzegovina'), ('BW', 'Botswana'), ('BV', 'Bouvet Island'), ('BR', 'Brazil'), ('IO', 'British Indian Ocean Territory'), ('BN', 'Brunei Darussalam'), ('BG', 'Bulgaria'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('KH', 'Cambodia'), ('CM', 'Cameroon'), ('CA', 'Canada'), ('CV', 'Cape Verde'), ('KY', 'Cayman Islands'), ('CF', 'Central African Republic'), ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CX', 'Christmas Island'), ('CC', 'Cocos (Keeling) Islands'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CG', 'Congo'), ('CD', 'Congo, The Democratic Republic of the'), ('CK', 'Cook Islands'), ('CR', 'Costa Rica'), ('CI', "Cote d'Ivoire"), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CY', 'Cyprus'), ('CZ', 'Czech Republic'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('ET', 'Ethiopia'), ('FK', 'Falkland Islands (Malvinas)'), ('FO', 'Faroe Islands'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GF', 'French Guiana'), ('PF', 'French Polynesia'), ('TF', 'French Southern Territories'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgia'), ('DE', 'Germany'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GR', 'Greece'), ('GL', 'Greenland'), ('GD', 'Grenada'), ('GP', 'Guadeloupe'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GG', 'Guernsey'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('HM', 'Heard Island and McDonald Islands'), ('VA', 'Holy See (Vatican City State)'), ('HN', 'Honduras'), ('HK', 'Hong Kong'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran, Islamic Republic of'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IM', 'Isle of Man'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JE', 'Jersey'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KP', "Korea, Democratic People's Republic of"), ('KR', 'Korea, Republic of'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', "Lao People's Democratic Republic"), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libyan Arab Jamahiriya'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MO', 'Macao'), ('MK', 'Macedonia, The Former Yugoslav Republic of'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshall Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('YT', 'Mayotte'), ('MX', 'Mexico'), ('FM', 'Micronesia, Federated States of'), ('MD', 'Moldova'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('AN', 'Netherlands Antilles'), ('NC', 'New Caledonia'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('NU', 'Niue'), ('NF', 'Norfolk Island'), ('MP', 'Northern Mariana Islands'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestinian Territory, Occupied'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PN', 'Pitcairn'), ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'), ('QA', 'Qatar'), ('RE', 'Reunion'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('BL', 'Saint Barthelemy'), ('SH', 'Saint Helena'), ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'), ('MF', 'Saint Martin'), ('PM', 'Saint Pierre and Miquelon'), ('VC', 'Saint Vincent and the Grenadines'), ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tome and Principe'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'), ('ZA', 'South Africa'), ('GS', 'South Georgia and the South Sandwich Islands'), ('ES', 'Spain'), ('LK', 'Sri Lanka'), ('SD', 'Sudan'), ('SR', 'Suriname'), ('SJ', 'Svalbard and Jan Mayen'), ('SZ', 'Swaziland'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syrian Arab Republic'), ('TW', 'Taiwan, Province of China'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania, United Republic of'), ('TH', 'Thailand'), ('TL', 'Timor-Leste'), ('TG', 'Togo'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TC', 'Turks and Caicos Islands'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('US', 'United States'), ('UM', 'United States Minor Outlying Islands'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VE', 'Venezuela'), ('VN', 'Viet Nam'), ('VG', 'Virgin Islands, British'), ('VI', 'Virgin Islands, U.S.'), ('WF', 'Wallis and Futuna'), ('EH', 'Western Sahara'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], max_length=100)),
                ('shipment_priority', models.CharField(blank=True, choices=[('Normal', 'Normal'), ('Fast', 'Fast'), ('Urgent', 'Urgent')], max_length=20, null=True)),
                ('total_amount', models.CharField(max_length=100)),
                ('shipment_mode', models.CharField(blank=True, choices=[('By Road', 'By Road'), ('By Air', 'By Air'), ('By Ship', 'By Ship')], max_length=100, null=True)),
                ('status', models.BooleanField(default=False)),
                ('sample_date', models.DateField(auto_now=True)),
                ('created_on', models.DateField(auto_now=True)),
                ('sample_2', models.CharField(blank=True, max_length=30, null=True)),
                ('item_quantity2', models.CharField(blank=True, max_length=30, null=True)),
                ('categories2', models.CharField(blank=True, max_length=30, null=True)),
                ('per_item_price2', models.CharField(blank=True, max_length=30, null=True)),
                ('sample_3', models.CharField(blank=True, max_length=30, null=True)),
                ('item_quantity3', models.CharField(blank=True, max_length=30, null=True)),
                ('categories3', models.CharField(blank=True, max_length=30, null=True)),
                ('per_item_price3', models.CharField(blank=True, max_length=30, null=True)),
                ('sample_4', models.CharField(blank=True, max_length=30, null=True)),
                ('item_quantity4', models.CharField(blank=True, max_length=30, null=True)),
                ('categories4', models.CharField(blank=True, max_length=30, null=True)),
                ('per_item_price4', models.CharField(blank=True, max_length=30, null=True)),
                ('sample_5', models.CharField(blank=True, max_length=30, null=True)),
                ('item_quantity5', models.CharField(blank=True, max_length=30, null=True)),
                ('categories5', models.CharField(blank=True, max_length=30, null=True)),
                ('per_item_price5', models.CharField(blank=True, max_length=30, null=True)),
                ('sample_6', models.CharField(blank=True, max_length=30, null=True)),
                ('item_quantity6', models.CharField(blank=True, max_length=30, null=True)),
                ('categories6', models.CharField(blank=True, max_length=30, null=True)),
                ('per_item_price6', models.CharField(blank=True, max_length=30, null=True)),
                ('sample_7', models.CharField(blank=True, max_length=30, null=True)),
                ('item_quantity7', models.CharField(blank=True, max_length=30, null=True)),
                ('categories7', models.CharField(blank=True, max_length=30, null=True)),
                ('per_item_price7', models.CharField(blank=True, max_length=30, null=True)),
                ('sample_8', models.CharField(blank=True, max_length=30, null=True)),
                ('item_quantity8', models.CharField(blank=True, max_length=30, null=True)),
                ('categories8', models.CharField(blank=True, max_length=30, null=True)),
                ('per_item_price8', models.CharField(blank=True, max_length=30, null=True)),
                ('sample_9', models.CharField(blank=True, max_length=30, null=True)),
                ('item_quantity9', models.CharField(blank=True, max_length=30, null=True)),
                ('categories9', models.CharField(blank=True, max_length=30, null=True)),
                ('per_item_price9', models.CharField(blank=True, max_length=30, null=True)),
                ('sample_10', models.CharField(blank=True, max_length=30, null=True)),
                ('item_quantity10', models.CharField(blank=True, max_length=30, null=True)),
                ('categories10', models.CharField(blank=True, max_length=30, null=True)),
                ('per_item_price10', models.CharField(blank=True, max_length=30, null=True)),
                ('sales_member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sample_lead', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Lead')),
                ('sample_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Product')),
            ],
        ),
    ]