from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import *

@admin.register(Product)
class PeroductAdmin(ImportExportModelAdmin):
    pass


# class LeadAdmin(ImportExportModelAdmin):
#     pass

# class AccountAdmin(admin.ModelAdmin):
# 	list_display = ['account_name','account_email','account_phone']
# 	ordering = ['account_name']
	

# class FeedbackAdmin(admin.ModelAdmin):
# 	list_display = ['name','email','rating','experience']
# 	ordering = ['rating']

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['user','user_phone',]

class EmailAdmin(admin.ModelAdmin):
	list_display = ['sender','Subject']
admin.site.register(Configuration)
admin.site.register(EmailCredentials)
admin.site.register(Sample)
admin.site.register(Packing)
admin.site.register(Category)
admin.site.register(Profile, UserProfileAdmin)
admin.site.register(Brief)
admin.site.register(BankDetails)
admin.site.register(Performa)
admin.site.register(Quotation)
admin.site.register(Lead)
admin.site.register(Contact)
admin.site.register(Opprtunity)
admin.site.register(Feedback)
#admin.site.register(EmailData, EmailAdmin)
admin.site.register(Document)
admin.site.register(Case)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Meeting)
admin.site.register(Task)
admin.site.register(Payment)
admin.site.register(Target)