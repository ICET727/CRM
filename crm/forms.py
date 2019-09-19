from django import forms
from django.contrib.auth.models import User
from .models import *
from django.forms import DateTimeInput,PasswordInput
class DateInput(forms.DateInput):
    input_type = 'date'
class UserForm(forms.ModelForm):
	#password = forms.CharField(widget = forms.PasswordInput())
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')


class UserProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ('user_phone','about','DOB','user_photo','email','password')
    widgets = {
              'password':PasswordInput(),
              'DOB':DateInput(),
            }   
# class AccountForm(forms.ModelForm):
#   #account_attachment = forms.
#   class Meta:
#       model = Account
#       fields = ('account_name', 'account_phone', 'account_email', 'website',
#                 'description', 'created_by',
#                 'address', 'street','account_attachment',
#                 'city', 'state',
#                 'postcode', 'country')

        # fields = '__all__'


class LeadForm(forms.ModelForm):
  class Meta:
      model = Lead
      fields = ('lead_name','lead_company','contacts','email','code','dob1',
                'phone','land_line','status','source','address','website','department',
                'street','city','state','postal_code','country','gst_number','currency_code',
                'description','attachment','attachment1','attachment2','designation','categories')
      exclude = ('user',)
      widgets = {
          'dob1': DateInput(),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('title','first_name','last_name','email',
                  'phone','description','contact_attachment')
        exclude = ('created_by',)


class OpportunityForm(forms.ModelForm):
  class Meta:
    model = Opprtunity
    field = ('name','stage','currency',
            'amount','lead_source','probability'
            'contacts','description','attachment')
    exclude = ('created_by',)
    
class DateInput(forms.DateInput):
    input_type = 'date'

class CaseForm(forms.ModelForm):

  class Meta:
    model = Case
    field = ('case_lead','case_name','date','case_type','description''attachment')#,'attachment1','attachment2')
    exclude = ('user','status')
    widgets = {
            'date': DateInput(),
        }

class DocumentForm(forms.ModelForm):
  #file = forms.FileField()
  class Meta:
    model = Document
    fields = ('name','file')
    exclude = ('user',)


class EmailForm(forms.ModelForm):
  class Meta:
    model = EmailData
    fields = ('sender','Subject','Body','file')
    exclude = ('user',)

# class OrderForm(forms.ModelForm):
#   class Meta:
#     model = Order
#     fields = ('order_lead','item_quantity',
#       'per_item_price','address','solubility','packaging','street','city','state','postal_code','ship_country',
#       'shipment_priority','uom','categories','attachment','attachment1','attachment2',
#       'product_code','code','gst_number','statutory','shipment_mode')
#     exclude = ('sales_member','total_amount','hsn')

class UploadFileForm(forms.Form):
    file = forms.FileField()

class OpportunityUpdateForm(forms.ModelForm):
  class Meta:
    model = Opprtunity
    field = ('id','name','stage','currency',
            'amount','lead_source','probability'
            'contacts','description','attachment')
    exclude = ('created_by',)


class LeadUpdateForm(forms.ModelForm):
  class Meta:
      model = Lead
      fields = ('lead_name','email',
                'phone','status','website',
                'description')
      exclude = ('user',)


class PaymentForm(forms.ModelForm):
  class Meta:
    model = Payment
    fields = ('invoice_id','transaction_id','order_name','leads','payment_date',
                'pay_amount','attachment','categories')
    exclude = ('created_by','total_amount','item_quantity',
              'product_hsn_code','status')
    widgets = {
            'payment_date': DateInput(),
        }

class ProductForm(forms.ModelForm):
 class Meta:
   model = Product
   fields = ('product_name','product_code','description','HSN_Number','packaging',
    'type1','UOM','tentative_dose','invoice_id','solubility')

class QuotationForm(forms.ModelForm):
  class Meta:
    model = Quotation
    fields = ("customer_code","customer_name","product_name","product_code","address","igst","payment_term","freight","price_per_50kg",
              "price_per_1kg","price_per_5kg","price_per_25kg","lead_term","delivery_term",
              'product2','code2','price_per_1kg2','price_per_5kg2','price_per_25kg2','price_per_50kg2',
              'product3','code3','price_per_1kg3','price_per_5kg3','price_per_25kg3','price_per_50kg3',
              'product4','code4','price_per_1kg4','price_per_5kg4','price_per_25kg4','price_per_50kg4',
              'product5','code5','price_per_1kg5','price_per_5kg5','price_per_25kg5','price_per_50kg5',
              'product6','code6','price_per_1kg6','price_per_5kg6','price_per_25kg6','price_per_50kg6',
              'product7','code7','price_per_1kg7','price_per_5kg7','price_per_25kg7','price_per_50kg7',
              'product8','code8','price_per_1kg8','price_per_5kg8','price_per_25kg8','price_per_50kg8',
              'product9','code9','price_per_1kg9','price_per_5kg9','price_per_25kg9','price_per_50kg9',
              'product10','code10','price_per_1kg10','price_per_5kg10','price_per_25kg10','price_per_50kg10',)
    exclude = ("user",)

class PerformaForm(forms.ModelForm):
  class Meta:
    model = Performa
    fields = ('customer_name','customer_contact','product_name','quantity','tentative_date',
      'per_item_price','freight','bank_name','insurance',
      'gst_number','pan_number','ecc','division','range1','payment_terms','remarks','delivere_terms',
      'product2','code2','per_item_price2','quantity2','product3','code3','per_item_price3','quantity3',
      'product4','code4','per_item_price4','quantity4','product5','code5','per_item_price5','quantity5',
      'product6','code6','per_item_price6','quantity6','product7','code7','per_item_price7','quantity7',
      'product8','code8','per_item_price8','quantity8','product9','code9','per_item_price9','quantity9',
      'product10','code10','per_item_price10','quantity10')
    exclude = ('user','total_amount','igsst_cost')
    widgets = {
            'tentative_date': DateInput(),
        }

class ProductBriefForm(forms.ModelForm):
  class Meta:
    model = Brief
    fields = ('new_product','application','tentative_rate','quantity_req','project_priority','form','criteria','solubility','mesh','tentative_consumption')