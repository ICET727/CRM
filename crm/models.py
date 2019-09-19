from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from .utils import *
from .validators import validate_file_extension
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class EmailCredentials(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	email = models.CharField((u'EMAIL_HOST_USER'),max_length=255)
	password = models.CharField((u'EMAIL_HOST_PASSWORD'),max_length=255)
class Configuration(models.Model):
	email_use_tls = models.BooleanField((u'EMAIL_USE_TLS'),default=True)
	email_host = models.CharField((u'EMAIL_HOST'),max_length=1024)
	email_port = models.PositiveSmallIntegerField((u'EMAIL_PORT'),default=587)

class Profile(models.Model):
	designation_choice = (('Sales Team','Sales Team'),
							('Dispatch Team','Dispatch Team'))
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	user_phone = PhoneNumberField(null=True,blank=True)
	user_photo = models.ImageField(null=True, blank=True, upload_to="user_photo/")
	DOB = models.DateField(null=True,blank=True)
	designation = models.CharField(max_length=500, blank=True, null=True,choices=designation_choice)
	about = models.TextField(max_length=1000,blank=True,null=True)
	email = models.CharField((u'EMAIL_HOST_USER'),max_length=255,blank=True, null=True)
	password = models.CharField((u'EMAIL_HOST_PASSWORD'),max_length=255,blank=True, null=True)

	# def __str__(self):
	# 	return self.designation
		
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	print(instance)
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Packing(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Category(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name



class Product(models.Model):
    uom_choice = (('N/A','N/A'),
                    ('KGS','KGS'),
                    ('LITRES','LITRES'))
    packaging_choice = (('KILO GRAM','KILO GRAM'),
                    ('BULK','BULK'),
                    ('5 KGS HDPE CAN','5 KGS HDPE CAN'),
                    ('25 KGS HDPE CAN','25 KGS HDPE CAN'),
                    ('50 KGS HDPE CAN','50 KGS HDPE CAN'),
                    ('FIBER DRUM OF 25KGS','FIBER DRUM OF 25KGS'))
    solubility_choices = (('Oil Soluable', 'Oil Soluable'),
    						('Water Soluable', 'Water Soluable'))
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    product_code = models.CharField(max_length=200)
    per_item_price = models.IntegerField(blank=True,null=True)
    solubility = models.CharField(max_length=50,choices=solubility_choices)
    HSN_Number = models.CharField(max_length=100)
    description = models.CharField(max_length=500,blank=True,null=True)
    packaging = models.ManyToManyField(Packing)
    type1 = models.CharField(max_length=500,blank=True,null=True)
    UOM = models.CharField(max_length=500,choices= uom_choice, blank=True,null=True)
    tentative_dose = models.CharField(max_length=500, blank=True,null=True)
    invoice_id = models.CharField(max_length=500, blank=True,null=True)

    def __str__(self):
    	return self.product_name +', '+ self.product_code


class Target(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	amount = models.CharField(max_length=100)
	def __str__(self):
		return self.amount
		

class Customer(models.Model):
	id = models.AutoField(primary_key=True)
	customer_name = models.CharField(max_length=200)
	email = models.EmailField()
	phone = PhoneNumberField(null=True)




class Contact(models.Model):
	contact_id = models.AutoField(primary_key=True)
	#user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100,null=True,blank=True)
	email = models.EmailField()
	phone = models.CharField(max_length=12)
	description = models.TextField(blank=True, null=True)
	created_by = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)
	created_on = models.DateField(auto_now=True)
	contact_active = models.BooleanField(default=True)
	contact_attachment = models.FileField(upload_to='ContactAttachment/', null=True, blank=True)

	def __str__(self):
		if self.first_name:
			return self.first_name +', '+self.title
		else:
			return self.title

class Lead(models.Model):
	categories_choice = (('Bakery','Bakery'),
					('Pharma','Pharma'),
					('Beverages','Beverages'),
					('Ice-Creams','Ice-Creams'),
					('Biscuits','Biscuits'),
					('Confectionary','Confectionary'),
					('B.C','B.C'),
					('Cookies','Cookies'),
					('SPF','SPF'))
	lead_id = models.AutoField(primary_key=True)
	# project name in lead name
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	contacts = models.ManyToManyField(Contact)
	lead_name = models.CharField(max_length=100,blank=True,null=True)
	first_name = models.CharField(max_length=100,null=True,blank=True)
	last_name = models.CharField(max_length=100,null=True,blank=True)
	code = models.CharField(max_length=100, unique=True)
	lead_company = models.CharField(max_length=100,null=True,blank=True)
	status = models.CharField(max_length=255, blank=True,null=True, choices=LEAD_STATUS, default="New")
	source = models.CharField(max_length=255,blank=True, null=True, choices=LEAD_SOURCE)
	phone = models.CharField(max_length=20, null=True,blank=True)
	land_line = models.CharField(max_length=20, null=True,blank=True)
	email = models.EmailField(blank=True,null=True)
	website = models.CharField(max_length=100,null=True,blank=True)
	address = models.CharField(max_length=100,null=True,blank=True)
	street =  models.CharField(max_length=100,null=True,blank=True)
	city = models.CharField(max_length=100,null=True,blank=True)
	dob1 = models.DateField()
	state =  models.CharField(max_length=100,null=True,blank=True)
	postal_code = models.IntegerField(blank=True,null=True)
	country = models.CharField(max_length=100, choices=COUNTRIES,null=True,blank=True)
	description = models.TextField(blank=True, null=True)
	attachment = models.FileField(upload_to='LeadAttach/', null=True, blank=True)
	attachment1 = models.FileField(upload_to='FSSAIL/', null=True, blank=True)
	attachment2 = models.FileField(upload_to='GST/', null=True, blank=True)
	created_on = models.DateTimeField(auto_now=True)
	designation = models.CharField(max_length=100,blank=True,null=True)
	categories = models.ManyToManyField(Category)
	lead_active = models.BooleanField(default=True)
	gst_number = models.CharField(max_length=200,null=True,blank=True)
	department = models.CharField(max_length=200,null=True,blank=True)
	#currency = models.CharField(max_length=200,null=True,blank=True,choices=CURRENCY_CODES)
	currency_code = models.CharField(max_length=200,choices=CURRENCY_CODES,default='INR')

	def __str__(self):
		if self.code:
			return self.lead_company +', '+ self.code+', '+ self.state+', '+self.city
		else:
			return self.lead_company+', '+ self.state+', '+self.city
	def get_complete_address(self):
		full_address = ""
		if self.street:
			if self.street:
				full_address += ", " + self.street
			else:
				full_address += self.street
		if self.city:
			if self.city:
				full_address += ", " + self.city
			else:
				full_address += self.city
		if self.state:
			if self.state:
				full_address += ", " + self.state
			else:
				full_address += self.state
		if self.country:
			if self.country:
				full_address += ", " + self.country
			else:
				full_address += self.country
		return full_address
	

class Order(models.Model):
	order_choice = (('Sample','Sample'),
					('Commercial','Commercial'))
	order_status = (('Yes','Yes'),
					('No','No'))
	solubility_choice = (('N/A','N/A'),
					('Water Soluble','Water Soluble'),
					('Oil Soluble','Oil Soluble'))
	packaging_choice = (('KILO GRAM','KILO GRAM'),
					('BULK','BULK'),
					('5 KGS HDPE CAN','5 KGS HDPE CAN'),
					('25 KGS HDPE CAN','25 KGS HDPE CAN'),
					('50 KGS HDPE CAN','50 KGS HDPE CAN'),
					('FIBER DRUM OF 25KGS','FIBER DRUM OF 25KGS'))
	categories_choice = (('Bakery','Bakery'),
					('Pharma','Pharma'),
					('Beverages','Beverages'),
					('Ice-Creams','Ice-Creams'),
					('Biscuits','Biscuits'),
					('Confectionary','Confectionary'),
					('B.C','B.C'),
					('SPF','SPF'))
	uom_choice = (('N/A','N/A'),
				('Litres','Litres'),
				('KGS','KGS'))
	shipment_choice = (('Normal','Normal'),
				('Fast','Fast'),
				('Urgent','Urgent'))
	shipment_mode = (('By Road','By Road'),('By Air','By Air'),('By Ship','By Ship'))
	# HSN = (('3302','3302'),
	# 				('No','No'))
	order_id = models.AutoField(primary_key=True)
	order_lead = models.ForeignKey(Lead,on_delete=models.CASCADE)
	sales_member = models.ForeignKey(User,on_delete=models.CASCADE)
	product_name = models.ForeignKey(Product,on_delete=models.CASCADE)
	#p_code = models.CharField(max_length=100,blank=True,null=True)
	item_quantity = models.IntegerField(blank=True,null=True)
	#hsn = models.IntegerField(blank=True,null=True)
	stage = models.CharField(max_length=64, choices=STAGES,default="APPROVAL")
	#order_type = models.CharField(max_length=30,choices=order_choice,blank=True,null=True)
	#solubility = models.CharField(max_length=30,choices=solubility_choice,blank=True)
	packaging = models.CharField(max_length=100)
	categories = models.ManyToManyField(Category)
	#code = models.CharField(max_length=100,blank=True,null=True)
	#uom = models.CharField(max_length=30,choices=uom_choice,blank=True)
	gst_number = models.CharField(max_length=30,unique=True)
	statutory = models.CharField(max_length=30,blank=True, null=True)
	per_item_price = models.IntegerField()
	address = models.CharField(max_length=100,blank=True,null=True)
	street = models.CharField(max_length=30,blank=True,null=True)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	postal_code = models.CharField(max_length=50)
	ship_country = models.CharField(max_length=100,choices=COUNTRIES)
	shipment_priority = models.CharField(max_length=20,choices=shipment_choice,blank=True,null=True)
	total_amount = models.CharField(max_length=100)
	shipment_mode = models.CharField(max_length=100, choices=shipment_mode, blank=True, null=True)
	status = models.BooleanField(default=False)
	#dispatch_status = models.BooleanField(default=False)
	attachment = models.FileField(upload_to='FSSAIL/', null=True, blank=True)
	attachment1 = models.FileField(upload_to='GST/', null=True, blank=True)
	attachment2 = models.FileField(upload_to='IEC/', null=True, blank=True)
	order_date = models.DateField(auto_now=True)
	created_on = models.DateField(auto_now=True)
	#===================================multiple=========
	product_2 = models.CharField(max_length=30,blank=True, null=True)
	code2 = models.CharField(max_length=30,blank=True, null=True)
	item_quantity2 = models.CharField(max_length=30,blank=True, null=True)
	categories2 = models.CharField(max_length=30,blank=True, null=True)
	per_item_price2 = models.CharField(max_length=30,blank=True, null=True)
	#product 3
	product_3 = models.CharField(max_length=30,blank=True, null=True)
	code3 = models.CharField(max_length=30,blank=True, null=True)
	item_quantity3 = models.CharField(max_length=30,blank=True, null=True)
	categories3 = models.CharField(max_length=30,blank=True, null=True)
	per_item_price3 = models.CharField(max_length=30,blank=True, null=True)
	# product 4
	product_4 = models.CharField(max_length=30,blank=True, null=True)
	code4 = models.CharField(max_length=30,blank=True, null=True)
	item_quantity4 = models.CharField(max_length=30,blank=True, null=True)
	categories4= models.CharField(max_length=30,blank=True, null=True)
	per_item_price4 = models.CharField(max_length=30,blank=True, null=True)
	#product 5
	product_5 = models.CharField(max_length=30,blank=True, null=True)
	code5 = models.CharField(max_length=30,blank=True, null=True)
	item_quantity5 = models.CharField(max_length=30,blank=True, null=True)
	categories5 = models.CharField(max_length=30,blank=True, null=True)
	per_item_price5 = models.CharField(max_length=30,blank=True, null=True)
	#product 6
	product_6 = models.CharField(max_length=30,blank=True, null=True)
	code6 = models.CharField(max_length=30,blank=True, null=True)
	item_quantity6 = models.CharField(max_length=30,blank=True, null=True)
	categories6 = models.CharField(max_length=30,blank=True, null=True)
	per_item_price6 = models.CharField(max_length=30,blank=True, null=True)
	#product 7
	product_7 = models.CharField(max_length=30,blank=True, null=True)
	code7 = models.CharField(max_length=30,blank=True, null=True)
	item_quantity7 = models.CharField(max_length=30,blank=True, null=True)
	categories7 = models.CharField(max_length=30,blank=True, null=True)
	per_item_price7 = models.CharField(max_length=30,blank=True, null=True)
	#product 8
	product_8 = models.CharField(max_length=30,blank=True, null=True)
	code8 = models.CharField(max_length=30,blank=True, null=True)
	item_quantity8 = models.CharField(max_length=30,blank=True, null=True)
	categories8 = models.CharField(max_length=30,blank=True, null=True)
	per_item_price8 = models.CharField(max_length=30,blank=True, null=True)
	#product 9
	product_9 = models.CharField(max_length=30,blank=True, null=True)
	code9 = models.CharField(max_length=30,blank=True, null=True)
	item_quantity9 = models.CharField(max_length=30,blank=True, null=True)
	categories9 = models.CharField(max_length=30,blank=True, null=True)
	per_item_price9 = models.CharField(max_length=30,blank=True, null=True)
	#product 10
	product_10 = models.CharField(max_length=30,blank=True, null=True)
	code10 = models.CharField(max_length=30,blank=True, null=True)
	item_quantity10 = models.CharField(max_length=30,blank=True, null=True)
	categories10 = models.CharField(max_length=30,blank=True, null=True)
	per_item_price10 = models.CharField(max_length=30,blank=True, null=True)

	def __str__(self):
		return str(self.product_name) +', '+str(self.order_lead)

	def get_complete_address(self):
		full_address = ""
		if self.address:
			full_address += self.address
		if self.street:
			if self.street:
				full_address += ", " + self.street
			else:
				full_address += self.street
		if self.city:
			if self.city:
				full_address += ", " + self.city
			else:
				full_address += self.city
		if self.state:
			if self.state:
				full_address += ", " + self.state
			else:
				full_address += self.state
		if self.ship_country:
			if self.ship_country:
				full_address += ", " + self.ship_country
			else:
				full_address += self.ship_country
		return full_address


class Track(models.Model):
	track_id = models.AutoField(primary_key=True)
	order_date = models.DateField(auto_now=True)
	delivery_date = models.DateField(auto_now=True)
	delivered = models.BooleanField(default=True)

	def __str__(self):
		return self.order_date

# class Account(models.Model):
# 	# ACCOUNT_STATUS_CHOICE = (
#  #        ("open", "Open"),
#  #        ('close', 'Close')
#  #    )
# 	account_id = models.AutoField(primary_key=True)
# 	account_name = models.CharField(max_length=100)
# 	account_email = models.EmailField()
# 	account_phone = PhoneNumberField(null=True)
# 	address = models.CharField(max_length=255, blank=True, null=True)
# 	street = models.CharField(max_length=100, blank=True, null=True)
# 	city = models.CharField(max_length=100, blank=True, null=True)
# 	state = models.CharField(max_length=100, blank=True, null=True)
# 	postcode = models.CharField(max_length=100, blank=True, null=True)
# 	country = models.CharField(max_length=100, choices=COUNTRIES,blank=True, null=True)
# 	website = models.URLField(blank=True, null=True)
# 	description = models.TextField(blank=True, null=True)
# 	created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
# 	created_on = models.DateTimeField(auto_now=True)
# 	account_active = models.BooleanField(default=True)
# 	account_attachment = models.FileField(upload_to='AccountFiles/', null=True,blank=True)

# 	def __str__(self):
# 		return self.account_name

# 	def get_complete_address(self):
# 		full_address = ""
# 		if self.address:
# 			full_address += self.address
# 		if self.street:
# 			if self.street:
# 				full_address += ", " + self.street
# 			else:
# 				full_address += self.street
# 		if self.city:
# 			if self.city:
# 				full_address += ", " + self.city
# 			else:
# 				full_address += self.city
# 		if self.state:
# 			if self.state:
# 				full_address += ", " + self.state
# 			else:
# 				full_address += self.state
# 		if self.country:
# 			if self.country:
# 				full_address += ", " + self.country
# 			else:
# 				full_address += self.country
# 		return full_address
# class Contact(models.Model):
# 	contact_id = models.AutoField(primary_key=True)
# 	#user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	title = models.CharField(max_length=100,null=True,blank=True)
# 	first_name = models.CharField(max_length=100,null=True,blank=True)
# 	last_name = models.CharField(max_length=100,null=True,blank=True)
# 	email = models.EmailField()
# 	phone = models.CharField(max_length=12,null=True)
# 	description = models.TextField(blank=True, null=True)
# 	created_by = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
# 	created_on = models.DateField(auto_now=True)
# 	contact_active = models.BooleanField(default=True)
# 	contact_attachment = models.FileField(upload_to='ContactAttachment/', null=True, blank=True)

# 	def __str__(self):
# 		if self.first_name and self.last_name:
# 			return self.first_name +" "+ self.last_name
# 		else:
# 			return self.title

class Opprtunity(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	lead = models.ForeignKey(Lead,on_delete=models.CASCADE,null=True)
	stage = models.CharField(max_length=64, choices=STAGES)
	currency = models.CharField(max_length=3, choices=CURRENCY_CODES, blank=True, null=True)
	amount = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
	lead_source = models.CharField(max_length=255,choices=SOURCES, blank=True, null=True)
	probability = models.IntegerField(default=0, blank=True, null=True)
	contacts = models.ManyToManyField(Contact)
	created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	created_on = models.DateField(auto_now=True)
	description = models.TextField(blank=True, null=True)
	opprtunity_active = models.BooleanField(default=True)
	attachment = models.FileField(upload_to='OpprtunityAttachment/',null=True, blank=True)

	def __str__(self):
		return self.name


class Feedback(models.Model):
	feedback_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	customer_name = models.ForeignKey(Lead, on_delete=models.CASCADE)
	email = models.EmailField()
	contact = models.CharField(max_length=13, null=True, blank=True)
	sample_letter = models.CharField(max_length=50, blank=True, null=True)
	#sample1
	sample1_name = models.CharField(max_length=1000, blank=True, null=True)
	comment1 = models.TextField(max_length=1000, blank=True, null=True)
	#sample2
	sample2_name = models.CharField(max_length=1000, blank=True, null=True)
	comment2 = models.TextField(max_length=1000, blank=True, null=True)
	#sample3
	sample3_name = models.CharField(max_length=1000, blank=True, null=True)
	comment3 = models.TextField(max_length=1000, blank=True, null=True)
	#sample4
	sample4_name = models.CharField(max_length=1000, blank=True, null=True)
	comment4 = models.TextField(max_length=1000, blank=True, null=True)
	#sample5
	sample5_name = models.CharField(max_length=1000, blank=True, null=True)
	comment5 = models.TextField(max_length=1000, blank=True, null=True)
	#sample6
	sample6_name = models.CharField(max_length=1000, blank=True, null=True)
	comment6 = models.TextField(max_length=1000, blank=True, null=True)
	#sample7
	sample7_name = models.CharField(max_length=1000, blank=True, null=True)
	comment7 = models.TextField(max_length=1000, blank=True, null=True)
	#sample8
	sample8_name = models.CharField(max_length=1000, blank=True, null=True)
	comment8 = models.TextField(max_length=1000, blank=True, null=True)
	#sample9
	sample9_name = models.CharField(max_length=1000, blank=True, null=True)
	comment9 = models.TextField(max_length=1000, blank=True, null=True)
	#sample10
	sample10_name = models.CharField(max_length=1000, blank=True, null=True)
	comment10 = models.TextField(max_length=1000, blank=True, null=True)
	description = models.TextField(max_length=1000, blank=True, null=True)

	def __str__(self):
		return str(self.customer_name)



class Case(models.Model):
	CASE_CHOICE = (
    ("New", "New"),
    ('Pending', 'Pending'),
    ('Closed', 'Closed'),
    ('Rejected', 'Rejected'),
    ('Duplicate', 'Duplicate'),
)
	case_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
	case_lead = models.ForeignKey(Lead,on_delete=models.CASCADE)
	case_name = models.CharField(max_length=100)
	date = models.DateField()
	case_type = models.CharField(max_length=100)
	description = models.TextField(max_length=2000, blank=True)
	status = models.CharField(max_length=100,choices=CASE_CHOICE,default='Pending')
	attachment = models.FileField(upload_to='Cases/', validators=[validate_file_extension]) #added 3 fields for attaching photos of damage
	#attachment1 = models.FileField(upload_to='Cases1/', validators=[validate_file_extension])
	#attachment2 = models.FileField(upload_to='Cases2/', validators=[validate_file_extension])

	def __str__(self):
		return self.case_name

class Document(models.Model):
	document_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	date = models.DateField(auto_now=True)
	name = models.CharField(max_length=100)
	file = models.FileField(upload_to='Document/', validators=[validate_file_extension])

	def __str__(self):
		return self.name


class EmailData(models.Model):

	email_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	sender = models.EmailField()
	Subject = models.CharField(max_length=100)
	Body = models.TextField()
	file = models.FileField(upload_to='Email/',blank=True, null=True)
	date = models.DateField(auto_now=True)

	def __str__(self):
		return self.sender

class Meeting(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	date = models.DateField()
	time = models.TimeField(auto_now=False, auto_now_add=False)
	description = models.CharField(max_length=1000)

	def __str__(self):
		return self.name



# class Meeting(models.Model):
# 	id = models.AutoField(primary_key=True)
# 	date = models.DateTimeField(auto_now=True)
# 	title = models.CharField(max_length=100)
# 	description = models.CharField(max_length=1000)

class Task(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=1000)
	start_date = models.DateField(auto_now=True)
	end_date = models.DateField()
	def __str__(self):
		return self.title






class Quotation(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    customer_name = models.ForeignKey(Lead,on_delete=models.CASCADE)
    customer_code = models.CharField(max_length=50)
    product_name = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_code = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=50,null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    address = models.CharField(max_length=500,blank=True,null=True)
    igst = models.CharField(max_length=200,blank=True,null=True)
    payment_term = models.CharField(max_length=200,blank=True,null=True)
    delivery_term = models.CharField(max_length=200,blank=True,null=True)
    lead_term = models.CharField(max_length=200,blank=True,null=True)
    date = models.DateField(auto_now=True)
    due_date = models.DateField(auto_now=True)
    freight = models.CharField(max_length=200,blank=True,null=True)
    price_per_1kg = models.CharField(max_length=50,blank=True,null=True)
    price_per_5kg = models.CharField(max_length=50,blank=True,null=True)
    price_per_25kg = models.CharField(max_length=50,blank=True,null=True)
    price_per_50kg = models.CharField(max_length=50,blank=True,null=True)
    # product two
    product2 = models.CharField(max_length=50,null=True,blank=True)
    code2 = models.CharField(max_length=50,null=True,blank=True)
    quantity2 = models.CharField(max_length=50,null=True,blank=True)
    price_per_1kg2 = models.CharField(max_length=50,blank=True,null=True)
    price_per_5kg2 = models.CharField(max_length=50,blank=True,null=True)
    price_per_25kg2 = models.CharField(max_length=50,blank=True,null=True)
    price_per_50kg2 = models.CharField(max_length=50,blank=True,null=True)
    #product 3
    product3 = models.CharField(max_length=50,null=True,blank=True)
    code3 = models.CharField(max_length=50,null=True,blank=True)
    quantity3 = models.CharField(max_length=50,null=True,blank=True)
    price_per_1kg3 = models.CharField(max_length=50,blank=True,null=True)
    price_per_5kg3 = models.CharField(max_length=50,blank=True,null=True)
    price_per_25kg3 = models.CharField(max_length=50,blank=True,null=True)
    price_per_50kg3 = models.CharField(max_length=50,blank=True,null=True)
    # product4
    product4 = models.CharField(max_length=50,null=True,blank=True)
    code4 = models.CharField(max_length=50,null=True,blank=True)
    quantity4 = models.CharField(max_length=50,null=True,blank=True)
    price_per_1kg4 = models.CharField(max_length=50,blank=True,null=True)
    price_per_5kg4 = models.CharField(max_length=50,blank=True,null=True)
    price_per_25kg4 = models.CharField(max_length=50,blank=True,null=True)
    price_per_50kg4 = models.CharField(max_length=50,blank=True,null=True)
    # product 5
    product5 = models.CharField(max_length=50,null=True,blank=True)
    code5 = models.CharField(max_length=50,null=True,blank=True)
    quantity5 = models.CharField(max_length=50,null=True,blank=True)
    price_per_1kg5 = models.CharField(max_length=50,blank=True,null=True)
    price_per_5kg5 = models.CharField(max_length=50,blank=True,null=True)
    price_per_25kg5 = models.CharField(max_length=50,blank=True,null=True)
    price_per_50kg5 = models.CharField(max_length=50,blank=True,null=True)
    # product 6
    product6 = models.CharField(max_length=50,null=True,blank=True)
    code6 = models.CharField(max_length=50,null=True,blank=True)
    quantity6 = models.CharField(max_length=50,null=True,blank=True)
    price_per_1kg6 = models.CharField(max_length=50,blank=True,null=True)
    price_per_5kg6 = models.CharField(max_length=50,blank=True,null=True)
    price_per_25kg6 = models.CharField(max_length=50,blank=True,null=True)
    price_per_50kg6 = models.CharField(max_length=50,blank=True,null=True)
    # product 7
    product7 = models.CharField(max_length=50,null=True,blank=True)
    code7 = models.CharField(max_length=50,null=True,blank=True)
    quantity7 = models.CharField(max_length=50,null=True,blank=True)
    price_per_1kg7 = models.CharField(max_length=50,blank=True,null=True)
    price_per_5kg7 = models.CharField(max_length=50,blank=True,null=True)
    price_per_25kg7 = models.CharField(max_length=50,blank=True,null=True)
    price_per_50kg7 = models.CharField(max_length=50,blank=True,null=True)
    # product 8
    product8 = models.CharField(max_length=50,null=True,blank=True)
    code8 = models.CharField(max_length=50,null=True,blank=True)
    quantity8 = models.CharField(max_length=50,null=True,blank=True)
    price_per_1kg8 = models.CharField(max_length=50,blank=True,null=True)
    price_per_5kg8 = models.CharField(max_length=50,blank=True,null=True)
    price_per_25kg8 = models.CharField(max_length=50,blank=True,null=True)
    price_per_50kg8 = models.CharField(max_length=50,blank=True,null=True)
    # product 9
    product9 = models.CharField(max_length=50,null=True,blank=True)
    code9 = models.CharField(max_length=50,null=True,blank=True)
    quantity9 = models.CharField(max_length=50,null=True,blank=True)
    price_per_1kg9 = models.CharField(max_length=50,blank=True,null=True)
    price_per_5kg9 = models.CharField(max_length=50,blank=True,null=True)
    price_per_25kg9 = models.CharField(max_length=50,blank=True,null=True)
    price_per_50kg9 = models.CharField(max_length=50,blank=True,null=True)
    # product 10
    product10 = models.CharField(max_length=50,null=True,blank=True)
    code10 = models.CharField(max_length=50,null=True,blank=True)
    quantity10 = models.CharField(max_length=50,null=True,blank=True)
    price_per_1kg10 = models.CharField(max_length=50,blank=True,null=True)
    price_per_5kg10 = models.CharField(max_length=50,blank=True,null=True)
    price_per_25kg10 = models.CharField(max_length=50,blank=True,null=True)
    price_per_50kg10 = models.CharField(max_length=50,blank=True,null=True)


class BankDetails(models.Model):
	id = models.AutoField(primary_key=True)
	account_name = models.CharField(max_length=100)
	bankers_name = models.CharField(max_length=100)
	account_number = models.IntegerField()
	ifsc_code = models.CharField(max_length=100)
	address = models.CharField(max_length=500)

	def __str__(self):
		return self.bankers_name


class Performa(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	customer_name = models.ForeignKey(Lead, on_delete=models.CASCADE)
	customer_contact = models.CharField(max_length=100)
	#customer_gst = models.CharField(max_length=100)
	product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	tentative_date = models.DateField()
	#payment_term = models.CharField(max_length=100)
	per_item_price = models.IntegerField()
	freight = models.CharField(max_length=100)
	igsst_cost = models.CharField(max_length=100, null=True,blank=True)
	total_amount = models.CharField(max_length=100, null=True,blank=True)
	bank_name = models.ForeignKey(BankDetails, on_delete=models.CASCADE)
	gst_number = models.CharField(max_length=100)
	pan_number = models.CharField(max_length=100)
	ecc = models.CharField(max_length=100)
	division = models.CharField(max_length=100,null=True,blank=True)
	range1 = models.CharField(max_length=100,null=True,blank=True)
	payment_terms = models.CharField(max_length=100,null=True,blank=True)
	delivere_terms = models.CharField(max_length=100,null=True,blank=True)
	remarks = models.CharField(max_length=100,null=True,blank=True)
	insurance = models.BooleanField(default=False)
	payment_status = models.BooleanField(default=False)
	#product2
	product2 = models.CharField(max_length=100,null=True,blank=True)
	code2 = models.CharField(max_length=100,null=True,blank=True)
	per_item_price2 = models.CharField(max_length=100,null=True,blank=True)
	quantity2 = models.CharField(max_length=100,null=True,blank=True)
	#product3
	product3 = models.CharField(max_length=100,null=True,blank=True)
	code3 = models.CharField(max_length=100,null=True,blank=True)
	per_item_price3 = models.CharField(max_length=100,null=True,blank=True)
	quantity3 = models.CharField(max_length=100,null=True,blank=True)
	#product4
	product4 = models.CharField(max_length=100,null=True,blank=True)
	code4 = models.CharField(max_length=100,null=True,blank=True)
	per_item_price4 = models.CharField(max_length=100,null=True,blank=True)
	quantity4 = models.CharField(max_length=100,null=True,blank=True)
	#product5
	product5 = models.CharField(max_length=100,null=True,blank=True)
	code5 = models.CharField(max_length=100,null=True,blank=True)
	per_item_price5 = models.CharField(max_length=100,null=True,blank=True)
	quantity5 = models.CharField(max_length=100,null=True,blank=True)
	#product6
	product6 = models.CharField(max_length=100,null=True,blank=True)
	code6 = models.CharField(max_length=100,null=True,blank=True)
	per_item_price6 = models.CharField(max_length=100,null=True,blank=True)
	quantity6 = models.CharField(max_length=100,null=True,blank=True)
	#product7
	product7 = models.CharField(max_length=100,null=True,blank=True)
	code7 = models.CharField(max_length=100,null=True,blank=True)
	per_item_price7 = models.CharField(max_length=100,null=True,blank=True)
	quantity7 = models.CharField(max_length=100,null=True,blank=True)
	#product8
	product8 = models.CharField(max_length=100,null=True,blank=True)
	code8 = models.CharField(max_length=100,null=True,blank=True)
	per_item_price8 = models.CharField(max_length=100,null=True,blank=True)
	quantity8 = models.CharField(max_length=100,null=True,blank=True)
	#product9
	product9 = models.CharField(max_length=100,null=True,blank=True)
	code9 = models.CharField(max_length=100,null=True,blank=True)
	per_item_price9 = models.CharField(max_length=100,null=True,blank=True)
	quantity9 = models.CharField(max_length=100,null=True,blank=True)
	#product10
	product10 = models.CharField(max_length=100,null=True,blank=True)
	code10 = models.CharField(max_length=100,null=True,blank=True)
	per_item_price10 = models.CharField(max_length=100,null=True,blank=True)
	quantity10 = models.CharField(max_length=100,null=True,blank=True)

	def __str__(self):
		return str(self.product_name)



class Payment(models.Model):
	categories_choice = (('Bakery','Bakery'),
					('Pharma','Pharma'),
					('Beverages','Beverages'),
					('Ice-Creams','Ice-Creams'),
					('Biscuits','Biscuits'),
					('Confectionary','Confectionary'),
					('B.C','B.C'),
					('SPF','SPF'))
	payment_id = models.AutoField(primary_key=True)
	invoice_id = models.CharField(max_length=500)
	transaction_id = models.CharField(max_length=500) #enabled unique field as true
	#payment_date = models.DateField(auto_now=True)
	#payment_amount = models.IntegerField()
	product_hsn_code = models.CharField(max_length=20,blank=True,null=True)
	order_name = models.ForeignKey(Performa,on_delete=models.CASCADE,related_name='o1')
	leads = models.ForeignKey(Lead,on_delete=models.CASCADE)
	payment_date = models.DateField(blank=True,null=True)
	pay_amount = models.IntegerField(default=0)
	due_amount = models.IntegerField(blank=True,null=True)
	created_by = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
	total_amount = models.IntegerField(blank=True,null=True)
	item_quantity = models.CharField(max_length=100, blank=True, null=True)
	#product_hsn_code = models.CharField(max_length=20,blank=True,null=True)
	attachment = models.FileField(upload_to='Payslip/',blank=True, null=True)
	categories = models.CharField(max_length=255,blank=True, null=True, choices=categories_choice)
	#payment_country = models.CharField(max_length=100,choices=COUNTRIES)
	status = models.BooleanField(default=False)
	def __str__(self):
		return self.transaction_id


class Brief(models.Model):
    project_choice = (('Normal','Normal'),
                ('Fast','Fast'),
                ('Urgent','Urgent'))
    mesh_choices = (('Yes','Yes'),
                ('No','No'))
    criteria_choices = (('Nature Identical','Nature Identical'),
                ('Natural','Natural'),
                ('Artificial','Artificial'))
    solubility_choices = (('Oil','Oil'),
                ('Water','Water'))
    new_product = models.CharField(max_length=500, blank=True, null=True)
    application = models.CharField(max_length=500, blank=True, null=True)
    tentative_rate = models.IntegerField()
    quantity_req = models.IntegerField()
    date = models.DateField(auto_now=True)
    project_priority = models.CharField(max_length=500,choices=project_choice, blank=True, null=True)
    form = models.CharField(max_length=500, blank=True, null=True)
    criteria = models.CharField(max_length=500, choices=criteria_choices,blank=True, null=True)
    solubility = models.CharField(max_length=500,choices=solubility_choices, blank=True, null=True)
    tentative_consumption =models.IntegerField()
    mesh = models.CharField(max_length=500,choices=mesh_choices, blank=True, null=True)
    def __str__(self):
        return str(self.new_product)



class Sample(models.Model):
    Sample_status = (('Yes','Yes'),
                    ('No','No'))
    categories_choice = (('Bakery','Bakery'),
                    ('Pharma','Pharma'),
                    ('Beverages','Beverages'),
                    ('Ice-Creams','Ice-Creams'),
                    ('Biscuits','Biscuits'),
                    ('Confectionary','Confectionary'),
                    ('Cookies','Cookies'),
                    ('Backery Customer','Backery Customer'),
                    ('B.C','B.C'),
                    ('SPF','SPF'))
    uom_choice = (('N/A','N/A'),
                ('Litres','Litres'),
                ('KGS','KGS'))
    shipment_choice = (('Normal','Normal'),
                ('Fast','Fast'),
                ('Urgent','Urgent'))
    shipment_mode = (('By Road','By Road'),('By Air','By Air'),('By Ship','By Ship'))
    solubility_choice = (('Oil Soluble','Oil Soluble'),
                ('Water Soluble','Water Soluble'))
    # HSN = (('3302','3302'),
    #               ('No','No'))
    id = models.AutoField(primary_key=True)
    sample_lead = models.ForeignKey(Lead,on_delete=models.CASCADE,blank=True,null=True)
    sales_member = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    sample_name = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    packaging = models.CharField(max_length=30,blank=True, null=True)
    stage = models.CharField(max_length=64, choices=STAGES,default="APPROVAL")
    #packaging = models.CharField(max_length=100, default="BULK")
    item_quantity = models.IntegerField()
    gst_number = models.CharField(max_length=30)
    statutory = models.CharField(max_length=30,blank=True, null=True)
    per_item_price = models.IntegerField()
    address = models.CharField(max_length=100,blank=True,null=True)
    street = models.CharField(max_length=30,blank=True,null=True)
    solubility = models.CharField(max_length=100, choices=solubility_choice, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    ship_country = models.CharField(max_length=100,choices=COUNTRIES)
    shipment_priority = models.CharField(max_length=20, choices=shipment_choice,blank=True,null=True)
    total_amount = models.CharField(max_length=100)
    shipment_mode = models.CharField(max_length=100, choices=shipment_mode, blank=True, null=True)
    status = models.BooleanField(default=False)
    sample_date = models.DateField(auto_now=True)
    created_on = models.DateField(auto_now=True)
#########################################################################################################
    sample_2 = models.CharField(max_length=30,blank=True, null=True)
    code2 = models.CharField(max_length=30,blank=True, null=True)
    packaging2 = models.CharField(max_length=30,blank=True, null=True)
    #categories2 = models.CharField(max_length=30,blank=True, null=True)
    per_item_price2 = models.CharField(max_length=30,blank=True, null=True)
    item_quantity2 = models.CharField(max_length=100,blank=True, null=True)
    # product3
    sample_3 = models.CharField(max_length=30,blank=True, null=True)
    code3 = models.CharField(max_length=30,blank=True, null=True)
    packaging3 = models.CharField(max_length=30,blank=True, null=True)
    #categories3 = models.CharField(max_length=30,blank=True, null=True)
    per_item_price3 = models.CharField(max_length=30,blank=True, null=True)
    item_quantity3 = models.CharField(max_length=100,blank=True, null=True)
    # product4
    sample_4 = models.CharField(max_length=30,blank=True, null=True)
    code4 = models.CharField(max_length=30,blank=True, null=True)
    packaging4 = models.CharField(max_length=30,blank=True, null=True)
    #categories4= models.CharField(max_length=30,blank=True, null=True)
    item_quantity4 = models.CharField(max_length=100,blank=True, null=True)
    per_item_price4 = models.CharField(max_length=30,blank=True, null=True)
    # product5
    item_quantity5 = models.CharField(max_length=100,blank=True, null=True)
    sample_5 = models.CharField(max_length=30,blank=True, null=True)
    code5 = models.CharField(max_length=30,blank=True, null=True)
    packaging5 = models.CharField(max_length=30,blank=True, null=True)
    #categories5 = models.CharField(max_length=30,blank=True, null=True)
    per_item_price5 = models.CharField(max_length=30,blank=True, null=True)
    # product 6
    sample_6 = models.CharField(max_length=30,blank=True, null=True)
    code6 = models.CharField(max_length=30,blank=True, null=True)
    packaging6 = models.CharField(max_length=30,blank=True, null=True)
    #categories6 = models.CharField(max_length=30,blank=True, null=True)
    per_item_price6 = models.CharField(max_length=30,blank=True, null=True)
    item_quantity6 = models.CharField(max_length=100,blank=True, null=True)
    # product 7
    sample_7 = models.CharField(max_length=30,blank=True, null=True)
    code7 = models.CharField(max_length=30,blank=True, null=True)
    packaging7 = models.CharField(max_length=30,blank=True, null=True)
    #categories7 = models.CharField(max_length=30,blank=True, null=True)
    per_item_price7 = models.CharField(max_length=30,blank=True, null=True)
    item_quantity7 = models.CharField(max_length=100,blank=True, null=True)
    # product 8
    sample_8 = models.CharField(max_length=30,blank=True, null=True)
    code8 = models.CharField(max_length=30,blank=True, null=True)
    packaging8 = models.CharField(max_length=30,blank=True, null=True)
    #categories8 = models.CharField(max_length=30,blank=True, null=True)
    per_item_price8 = models.CharField(max_length=30,blank=True, null=True)
    item_quantity8 = models.CharField(max_length=100,blank=True, null=True)
    # product 9
    sample_9 = models.CharField(max_length=30,blank=True, null=True)
    code9 = models.CharField(max_length=30,blank=True, null=True)
    packaging9 = models.CharField(max_length=30,blank=True, null=True)
    #categories9 = models.CharField(max_length=30,blank=True, null=True)
    per_item_price9 = models.CharField(max_length=30,blank=True, null=True)
    item_quantity9 = models.CharField(max_length=100,blank=True, null=True)
    # product 9
    sample_10 = models.CharField(max_length=30,blank=True, null=True)
    code10 = models.CharField(max_length=30,blank=True, null=True)
    packaging10 = models.CharField(max_length=30,blank=True, null=True)
    #categories10 = models.CharField(max_length=30,blank=True, null=True)
    per_item_price10 = models.CharField(max_length=30,blank=True, null=True)
    item_quantity10 = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return str(self.sample_name) +', '+str(self.sample_lead)
    
    def get_complete_address(self):
        full_address = ""
        if self.address:
            full_address += self.address
        if self.street:
            if self.street:
                full_address += ", " + self.street
            else:
                full_address += self.street
        if self.city:
            if self.city:
                full_address += ", " + self.city
            else:
                full_address += self.city
        if self.state:
            if self.state:
                full_address += ", " + self.state
            else:
                full_address += self.state
        if self.ship_country:
            if self.ship_country:
                full_address += ", " + self.ship_country
            else:
                full_address += self.ship_country
        return full_address