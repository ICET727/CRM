from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               , login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import EmailMessage
from rest_framework import viewsets
from django.db import transaction
from datetime import datetime , timedelta
import smtplib
now = datetime.now()
today = now.date()
tom_day = datetime.strftime(datetime.now() + timedelta(1), '%Y-%m-%d')
day_1 = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
day_2 = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')
day_3 = datetime.strftime(datetime.now() - timedelta(3), '%Y-%m-%d')
day_4 = datetime.strftime(datetime.now() - timedelta(4), '%Y-%m-%d')
from django.http import JsonResponse
from django.db.models import Sum
date_from = now.month-1
date_to = now.month
import phonenumbers
from django.core import serializers
import operator
from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			print("Hello")
			Token.objects.filter(user=user).delete()
			token = Token.objects.create(user=user)
			if user.is_superuser:
				login(request,user)
				return redirect('/dash-test')
			else:
				profile = Profile.objects.get(user=user).designation
				if profile == "Sales Team":
					login(request,user)
					return redirect('/sales/profile')
				if profile == "Dispatch Team":
					login(request,user)
					return redirect('/dispatch/profile')
		else:
			return HttpResponseRedirect('/accounts/login')
	return render(request, 'index.html',{})

def Dispatch_Person(request, id=''):
	if id:
		n = len(id)
		a = int(id[:n-1])
		if int(id[-1]):
			Order.objects.filter(order_id=a).update(stage='DISPATCHED')
			return redirect('/dispatch/profile')
		#print(int(id[-1]))
	orders = Order.objects.filter(stage="SENT FOR PRODUCTION")
	return render(request,'dispatch_profile.html',{"orders":orders})


def validate_user(request):
	username = request.GET.get('username')
	password = request.GET.get('password')
	mail = request.GET.get('mail')
	if mail:
		user = User.objects.get(username=mail)
		if user:
			return JsonResponse({"check":True})
	else:
		if authenticate(username=username, password=password):
			return JsonResponse({"data":True})
		return JsonResponse({"data":False})

@login_required
def order_name(request):
	customer_id = request.GET.get('customer_id')
	customer = Lead.objects.get(lead_id=customer_id)
	customer_code = customer.code
	orders = Performa.objects.filter(payment_status=False,customer_name=customer)
	#print(orders)
	cat = customer.categories.all()[0].name
	ids = []
	codes = []
	name = []
	for i in orders:
		ids.append(i.id)
		codes.append(i.product_name.product_code)
		name.append(i.product_name.product_name)
	return JsonResponse({"codes":codes,"names":name,"cat":cat,"ids":ids})

# def order_category(request):
# 	customer_code = request.GET.get(customer_code)
# 	customer = Lead.objects.get(lead_id=customer_id)
@login_required
def Amount(request):
	performa_id = request.GET.get('id')
	amount = Performa.objects.get(id=performa_id).total_amount
	return JsonResponse({"amount":amount})

@login_required
def customer_data(request):
	id = request.GET.get('customer_id')
	#print(customer_code)
	d = Lead.objects.get(lead_id=id)
	orders = Order.objects.filter(order_lead=d)
	pre = []
	for i in orders:
		pre.append(i.product_name.product_name)
	data = d.code
	state = d.state
	country = d.country
	postal_code = d.postal_code
	context = {
			"data":data,
			"state":state,
			"country":country,
			"postal_code":postal_code,
			"city":d.city,
			"previous_data":pre
	}

	return JsonResponse(context)

@login_required
def customer_order(request):
	id = request.GET.get('customer_id')
	#print(customer_code)
	d = Lead.objects.get(lead_id=id)
	#orders = Order.objects.filter(order_lead=d)
	pre = []
	# for i in orders:
	# 	pre.append(i.product_code.product_name)
	data = d.code
	#print(d.postal_code)
	gst = d.gst_number
	state = d.state
	country = d.country
	postal_code = d.postal_code
	context = {
			"data":data,
			"state":state,
			"country":country,
			"postal_code":postal_code,
			"city":d.city,
			"previous_data":pre,
			"street": d.street,
			"f_address": d.address,
			"gst":gst
	}

	return JsonResponse(context)

@login_required
def quotation_data(request):
	customer_id = request.GET.get('customer_id')
	customer = Lead.objects.get(lead_id=customer_id)
	customer_code = customer.code
	#print(customer_code)
	customer_name = customer.lead_company
	address = customer.get_complete_address()
	return JsonResponse({"data":customer_code,"name":customer_name,"address":address})

@login_required
def product_data(request):
	product_id = request.GET.get('p_id')
	product_code = request.GET.get('code')
	if product_id:
		product = Product.objects.get(id=product_id)
		product_code = product.product_code
		price = product.per_item_price
		solubility = product.solubility
		packaging = product.packaging.all()
		p = []
		for i in packaging:
			p.append(i.name)
		print(p)
		if product.UOM:
			uom = product.UOM
			print(uom)
		else:
			uom = "KGS"
		#print(customer_code)
		#product_name = product.lead_company
		#address = customer.get_complete_address()
		return JsonResponse({"data":product_code,"packaging":p,"uom":uom,"price":price,"solubility":solubility})
	if product_code:
		product = Product.objects.get(product_code=product_code).product_name
		return JsonResponse({"data":product})

@login_required
def target(request):
	amount = request.GET.get('amount')
	user1 = request.GET.get('user')
	user = User.objects.get(username=user1)
	if amount:
		t = Target(user=user,amount=amount)
		t.save()
		return JsonResponse({"data":True})
	else:
		return JsonResponse({"data":False})

@login_required
def order_notifications(request):
	orders = Order.objects.filter(created_on__gte=day_3,created_on__lte=today)
	case = Case.objects.filter(date__gte=day_4,date__lte=today)
	return render(request,'notification.html',{"orders":orders,"case":case})

@login_required
def user_logout(request):
    logout(request)
    return redirect("/accounts/login")

@login_required
@user_passes_test(lambda u: u.is_superuser)
def adminCall(request):
	user = request.user
	#print(date_from)
	all_data = User.objects.all()
	profile = Profile.objects.filter(user=user)
	sales_persons = User.objects.filter(is_staff=False,is_superuser=False)
	last_month_sales = Payment.objects.filter(status=True).aggregate(Sum('total_amount'))
	print(last_month_sales)
	if last_month_sales['total_amount__sum']:
		sales = round(last_month_sales['total_amount__sum'],2)
	else:
		sales = 0
	last_month_orders = Order.objects.all().count()
	last_month_leads = Lead.objects.all().count()
	#print(last_month_leads)
	total_feedbacks = Feedback.objects.all().count()
	context = {
			'profile': profile,
			'user': user,
			'sales': sales_persons,
			"last_month_sales":sales,
			"last_month_orders":last_month_orders,
			"last_month_leads":last_month_leads,
			"total_feedbacks":total_feedbacks,
			"all_data":all_data
	}
	
	return render(request, 'dash-test.html',context)

@login_required
def memberHome(request):
	user1 = request.user
	
	profile = Profile.objects.get(user=user1)
	targets = Target.objects.filter(user=user1)
	t = len(targets)
	samples_number = Order.objects.filter(sales_member=user1,status=True).count()
	leads_number = Lead.objects.filter(user=user1).count()
	#print(Order.objects.filter(sales_member=user1,order_type='Sample'))
	pending_order = Order.objects.filter(sales_member=user1,stage="APPROVAL").count()
	complete_order = Order.objects.filter(sales_member=user1,stage="DELIVERED").count()
	monthly_leads = Lead.objects.filter(user=user1,created_on__month__gte=date_from).count()
	last_month_sales = Payment.objects.filter(created_by=user1,status=True,payment_date__month__lte=now.month,payment_date__month__gte=date_from).aggregate(Sum('total_amount'))
	#monthly_sales = Order.objects.filter(sales_member=user1,status="Yes").aggregate(Sum('total_amount'))
	print(last_month_sales)
	if t:
		target = targets[t-1]
		if last_month_sales['total_amount__sum']:
			sales = round(last_month_sales['total_amount__sum'],2)
			remaining = int(target.amount) - sales
			percentage = (sales/int(target.amount))*100
	else:
		target = 0
		sales = 0
		remaining = target
		percentage = 0
	# print(target)
	#target = remaining = target 
	#sales = 5000#round(last_month_sales['total_amount__sum'],2)
	#remaining = int(target.amount) - sales
	#percentage = (sales/int(target.amount))*100
	orders = Order.objects.filter(sales_member=user1)
	this_month_sales = Payment.objects.filter(created_by=user1,status=True,payment_date__month__lte=now.month).aggregate(Sum('total_amount'))
	reject_product_order = Order.objects.filter(sales_member=user1,stage="REJECTED").count()
	sample_amount = Sample.objects.filter(sales_member=user1,created_on__month__lte=date_to,created_on__month__gte=date_from).aggregate(Sum('total_amount'))
	context ={
		"sample_amount":sample_amount,
		"profile": profile,
		"user1": user1,
		"samples_number": samples_number,
		"leads_number":leads_number,
		"pending_order":pending_order,
		"complete_order":complete_order,
		"monthly_leads":monthly_leads,
		"last_month_sales":sales,
		"orders":orders,
		"this_month_sales":this_month_sales,
		"reject_product_order":reject_product_order,
		"target":target,
		"remaining":remaining,
		"percentage": percentage
	}
	return render(request, 'profile.html',context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def SalesProfile(request, name=''):
	user1 = User.objects.get(username=name)

	profile = Profile.objects.filter(user=user1)

	targets = Target.objects.filter(user=user1)
	t = len(targets)
	if t:
		target = targets[t-1]
	else:
		target = targets

	profile = Profile.objects.get(user=user1)
	samples_number = Order.objects.filter(sales_member=user1,status=True).count()
	leads_number = Lead.objects.filter(user=user1).count()
	#print(Order.objects.filter(sales_member=user1,order_type='Sample'))
	pending_order = Order.objects.filter(sales_member=user1,status=False).count()
	complete_order = Order.objects.filter(sales_member=user1,status=True).count()
	monthly_leads = Lead.objects.filter(user=user1,created_on__month__gte=date_from).count()
	last_month_sales = Order.objects.filter(sales_member=user1,status=True,created_on__month__lte=date_from,created_on__month__gte=now.month).aggregate(Sum('total_amount'))
	#monthly_sales = Order.objects.filter(sales_member=user1,status="Yes").aggregate(Sum('total_amount'))
	#print(monthly_sales)
	orders = Order.objects.filter(sales_member=user1)
	this_month_sales = Payment.objects.filter(created_by=user1,status=True,payment_date__month__lte=now.month).aggregate(Sum('total_amount'))
	complete_product_order = Order.objects.filter(sales_member=user1,status=True).count()
	sample_amount = Sample.objects.filter(sales_member=user1,created_on__month__lte=date_to,created_on__month__gte=date_from).aggregate(Sum('total_amount'))
	#print(user1.first_name)
	if last_month_sales['total_amount__sum']:
		sales = round(last_month_sales['total_amount__sum'],2)
		remaining = int(target.amount) - sales
		percentage = (sales/int(target.amount))*100
	else:
		sales = 0
		remaining = target
		percentage = 0


	context ={
		"sample_amount":sample_amount,
		"profile": profile,
		"user1": user1,
		"samples_number": samples_number,
		"leads_number":leads_number,
		"pending_order":pending_order,
		"complete_order":complete_order,
		"monthly_leads":monthly_leads,
		"last_month_sales":sales,
		"orders":orders,
		"this_month_sales":this_month_sales,
		"complete_product_order":complete_product_order,
		"remaining": remaining,
		"target": target
	}
	return render(request, 'visit_profile.html', context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def Usercreate(request):
	if request.method == 'POST':
		username = request.POST.get('email')
		password = request.POST.get('password')
		designation = request.POST.get('designation')
		#print(designation)
		user = User.objects.filter(username=username)
		#print(user)
		if user:
			#print("Hello")
			return redirect('/user/create')
		else:
			user = User.objects.create_user(username=username,email=username,password=password)
			profile = Profile.objects.filter(user=user).update(designation=designation)
			if user:
				url = 'http://127.0.0.1:8000/update/profile'
				subject = 'User Registration'
				message = 'Hi\n Your account has been created with Amar Bio Organics Pvt. Ltd. \n Please visit the link below to edit your profile.\n'+ url +'\n Your email: ' + username + '\n password: ' + password +'\n\n\n\n Thanks & Regards'
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [username,]
				send_mail(subject,message,email_from,recipient_list)

	return render(request,'create_member1.html')

@login_required
@transaction.atomic
def update_profile(request):
	user = request.user
	if request.method == "POST":
		user_form = UserForm(request.POST, instance=request.user)
		profile_form = UserProfileForm(request.POST,request.FILES, instance=request.user.profile,)
		#print(profile_form)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return redirect('/sales/profile')
		else:
			# messages.error(request, _('Please correct the error below.'))
			return HttpResponse("error")
	else:
		user_form = UserForm(instance=request.user)
		profile_form = UserProfileForm(instance=request.user.profile)

	context = {
				'user_form': user_form,
				'profile_form': profile_form
	}
	if user.is_superuser:
		return render(request,'update_profile_admin.html', context)
	else:
		return render(request,'update_profile.html', context)

def mail_check(request):
	user = request.user
	email = request.GET.get('email')
	password = request.GET.get('password')
	configuration = Configuration.objects.all()
	if len(configuration)>0:
		email_use_tls = configuration[0].email_use_tls
		email_host = configuration[0].email_host
		email_port = configuration[0].email_port

	smtpObj = smtplib.SMTP(email_host,email_port)
	smtpObj.starttls()
	try:
		a = smtpObj.login(email,password)
		return JsonResponse({"data":True})
	except smtplib.SMTPAuthenticationError:
		return JsonResponse({"data":False})
	

def account_form(request):
	if request.method == "POST":
		form = AccountForm(request.POST)
		#print("Hello")
		#form = TagForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Success")
	else:
		form = AccountForm()
		#form = TagForm()
	return render(request,'account_form.html',{'form':form})

def account_list(request):
	ac = Account.objects.all()
	#print(ac)
	#
		#print(i.get_complete_address)
	#print(ac.account_name)
	return render(request,'account_list.html',{'ac':ac})

@login_required
def lead_form(request):
	user = request.user
	contacts1 = Contact.objects.all()
	form = LeadForm()
	if request.method == "POST":
		if request.FILES:
			form = LeadForm(request.POST, request.FILES)
			#print(request.FILES)
		else:
			form = LeadForm(request.POST)
		if form.is_valid():
			obj = form.save()
			obj.user = request.user
			obj.save()
			return redirect("/customer/list")
	else:
		form = LeadForm()
	profile = Profile.objects.get(user=user)
	context = {
				'form': form,
				'profile': profile,
				'contacts1': contacts1,
	}
	return render(request, 'lead_form.html',context)
@login_required
def lead_list(request, name=''):
	if not name:
		user = request.user
		lead = Lead.objects.filter(user=user)
	else:
		login_user = request.user
		if login_user.is_superuser:
			user = User.objects.get(username=name)
			lead = Lead.objects.filter(user=user)
		else:
			return HttpResponse("You Don't Have Permission To Access It.")
	profile = Profile.objects.get(user=user)
	context = {
				'lead': lead,
				'profile': profile
	}
	return render(request,'lead_list.html',context)
@login_required
def opprtunity_form(request):
	if request.method == 'POST':
		if request.FILES:
			form = OpportunityForm(request.POST, request.FILES)
		else:
			form = OpportunityForm(request.POST)
		if form.is_valid():
			obj = form.save()
			obj.created_by = request.user
			#print(obj.created_by)
			obj.save()
			return redirect("/opportunity/list")
	else:
		form = OpportunityForm()
	return render(request,'opportunity_form.html',{'form':form})
@login_required
def opportunity_list(request, name=''):
	if not name:
		user = request.user
	else:
		user = User.objects.get(username=name)
	if request.method =="POST":
		form = OpportunityUpdateForm(request.POST)
		id = form['contacts'].value()[0]
		#print(id)
		name = form['name'].value()
		lead = form['lead'].value()
		#print(lead)
		stage = form['stage'].value()
		#print(stage)
		probability = form['probability'].value()
		amount = form['amount'].value()
		description = form['description'].value()
		l1 = Lead.objects.get(lead_name=lead)
		#print(l1)
		Opprtunity.objects.filter(id=int(id)).update(name=name,lead=l1,stage=stage,
			probability=probability,amount=amount,description=description)
	opportunity = Opprtunity.objects.filter(created_by=user)
	return render(request,'opportunity_list.html',{'opportunity':opportunity})

def contact_form(request):
	if request.method == 'POST':
		if request.FILES:
			form = ContactForm(request.POST, request.FILES)
			#print(request.FILES)
		else:
			form = ContactForm(request.POST)
		if form.is_valid():
			obj = form.save()
			obj.created_by = request.user
			#print(obj.created_by)
			obj.save()
			return redirect("/contact/list")
	else:
		form = ContactForm()
	return render(request,'contact_form.html',{'form':form})
@login_required
def contact_list(request, name=''):
	if not name:
		user = request.user
	else:
		user = User.objects.get(username=name)
	contact = Contact.objects.filter(created_by=user)
	return render(request, 'contact_list.html',{'contact':contact})


def feedback(request):
	leads = Lead.objects.all()
	user = request.user
	if request.method == 'POST':
		name = request.POST.get('customer_name')
		customer_name = Lead.objects.get(lead_id=name)
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		sample = request.POST.get('sample_1')
		sample_1 = Sample.objects.get(id=sample).sample_name
		review1 = request.POST.get('review1')
		sample_2 = request.POST.get('sample_2')
		review2 = request.POST.get('review2')
		sample_3 = request.POST.get('sample_3')
		review3 = request.POST.get('review3')
		sample_4 = request.POST.get('sample_4')
		review4 = request.POST.get('review4')
		sample_5 = request.POST.get('sample_5')
		review5 = request.POST.get('review5')
		sample_6 = request.POST.get('sample_6')
		review6 = request.POST.get('review6')
		sample_7 = request.POST.get('sample_7')
		review7 = request.POST.get('review7')
		sample_8 = request.POST.get('sample_8')
		review8 = request.POST.get('review8')
		sample_9 = request.POST.get('sample_9')
		review9 = request.POST.get('review9')
		sample_10 = request.POST.get('sample_10')
		review10 = request.POST.get('review10')
		sample_letter = request.POST.get('sample_letter')
		description = request.POST.get('description')
		#print(rating)
		q = Feedback(user=user,customer_name=customer_name,email=email,contact=phone,description=description,
			sample_letter=sample_letter,
			sample1_name=sample_1,comment1=review1,sample2_name=sample_2,comment2=review2,
			sample3_name=sample_3,comment3=review3,sample4_name=sample_4,comment4=review4,
			sample5_name=sample_5,comment5=review5,sample6_name=sample_6,comment6=review6,
			sample7_name=sample_7,comment7=review7,sample8_name=sample_8,comment8=review8,
			sample9_name=sample_9,comment9=review9,sample10_name=sample_10,comment10=review10)
		q.save()
		return redirect('/feedback/list')

	return render(request,'feedback_form.html',{"leads":leads})


	
def admin_feedback_information(request,id):
	feedback = Feedback.objects.get(feedback_id=id)
	return render(request,"admin_feedback_information.html",{"feedback":feedback})

def feedback_data(request):
	customer_id = request.GET.get("id")
	user = request.user
	customer = Lead.objects.get(lead_id=customer_id)
	email = customer.email
	contact = customer.phone
	s = Sample.objects.filter(sales_member=user,sample_lead=customer)
	ids = []
	samples = []
	for i in s:
		samples.append(str(i.sample_name))
		ids.append(i.id)
	context = {
		"email":email,
		"contact":contact,
		"samples":samples,
		"ids":ids,
	}

	return JsonResponse(context)

def all_sample(request):
	sampe_id = request.GET.get("id")
	s = Sample.objects.get(id=sampe_id)
	s2 = s.sample_2
	s3 = s.sample_3
	s4 = s.sample_4
	s5 = s.sample_5
	s6 = s.sample_6
	s7 = s.sample_7
	s8 = s.sample_8
	s9 = s.sample_9
	s10 = s.sample_10
	 

	context = {
		"data":True,
		"s2":s2,
		"s3":s3,
		"s4":s4,
		"s5":s5,
		"s6":s6,
		"s7":s7,
		"s8":s8,
		"s9":s9,
		"s10":s10,
	}
	return JsonResponse(context)
	
@login_required
def document_create(request):
	#form = DocumentForm()
	if request.method == "POST":
		#print("Hello")
		form = DocumentForm(request.POST, request.FILES)
		#print("Hello")
		#prform)
		if form.is_valid():
			obj = form.save()
			
			obj.user = request.user
			#print(obj.user)
			#obj = Document(user=user,name=request.POST.get("name"),file=request.FILES['file'])
			obj.save()
			return redirect('/document/list')
	else:
		form = DocumentForm()
	return render(request, 'document_form.html', {'form': form})


@api_view(['GET', 'POST'])
def email_list(request):
	if request.method == "GET":
		emails = Email.objects.all()
		serializer = EmailSerializer(emails,many=True)
		return Response(serializer.data)

	elif request.method == "POST":
		serializer = EmailSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			email = serializer['sender'].value
			subject = serializer['Subject'].value
			message = serializer['Body'].value
			#print(type(message))
			attach = request.data['file']
			#print(attach.name)
			try:
				mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
				mail.attach(attach.name, attach.read(), attach.content_type)
				#print("Hello")
				mail.send()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			except:
				return Response("Mail Failed")
			#email_from = settings.EMAIL_HOST_USER
			#recipient_list = [,]
			#send_mail(subject,message,email_from,recipient_list)
			
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required
def email_send(request):
	form = EmailForm()
	user = request.user
	if request.method == "POST":
		if request.FILES:
			form = EmailForm(request.POST,request.FILES)
		else:
			form = EmailForm(request.POST)
		if form.is_valid():
			#print(request.POST.get('Subject'))
			email = request.POST.get('sender')
			subject = request.POST.get('Subject')
			message = request.POST.get('Body')
			if request.FILES:
				attach = request.FILES['file']
				try:
					mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
					mail.attach(attach.name, attach.read(), attach.content_type)
					a=mail.send()
				except:
					return HttpResponse("Mail Failed")
			else:
				recipient_list = [email,]
				send_mail(subject,message,settings.EMAIL_HOST_USER,recipient_list)

			obj = form.save()
			obj.user = request.user
			obj.save()	
			return redirect('/email/list')
	else:
		form = EmailForm()
	if user.is_superuser:
		return render(request, 'super_user_mail.html',{'form':form})
	else:
		return render(request, 'chatter.html',{'form':form})
		
	


@login_required
def email_list(request):
	user = request.user
	emails = EmailData.objects.filter(user=user)
	#print(emails)
	if user.is_superuser:
		return render(request, 'super_user_email_list.html',{'emails':emails})
		#return HttpResponse("Hello")
	else:
		return render(request, 'email_list.html',{'emails':emails})		


@login_required
def case(request):
	form = CaseForm()
	if request.method == "POST":
		if request.FILES:
			form = CaseForm(request.POST, request.FILES)
		else:
			form = CaseForm(request.POST)
		if form.is_valid():
			obj = form.save()
			obj.user = request.user
			obj.save()
			return redirect('/case/list')
	else:
		form = CaseForm()
	return render(request, 'case_form.html', {'form':form})
@login_required
def case_list(request, name=''):
	if not name:
		user = request.user
	else:
		user = User.objects.get(username=name)
		if not user:
			return HttpResponse("User is not found")
	cases = Case.objects.filter(user=user)
	return render(request, 'case_list.html',{'cases':cases})

def case_status(request,id=''):
	user = request.user
	if id:
		n = len(id)
		a = int(id[:n-1])
		if int(id[-1])==0:
			Case.objects.filter(case_id=a).update(status="Closed")
			return redirect('/case/list')
	cases = Case.objects.filter(user=user)
	return render(request, 'case_list.html',{'cases':cases})

@login_required
def document_list(request):
	user = request.user
	docs = Document.objects.filter(user=user)
	context = {
		'docs' : docs
	}
	return render(request, 'document_list.html', context)
	
@login_required
@user_passes_test(lambda u: u.is_superuser)
def SalesPersonProfile(request, username):
	user1 = User.objects.get(username=username)
	closed_won=Order.objects.filter(sales_member=user1,stage="DELIVERED").count()
	analysis=Order.objects.filter(sales_member=user1,stage="APPROVAL").count()
	closed_lost=Order.objects.filter(sales_member=user1,stage="REJECTED").count()
	dispatched =Order.objects.filter(sales_member=user1,stage="DISPATCHED").count()
	perposal=Order.objects.filter(sales_member=user1,stage="SENT FOR PRODUCTION").count()
	lead = Lead.objects.filter(user=user1)
	# opportunity = Order.objects.filter(created_by=user1)
	contacts = Contact.objects.filter(created_by=user1)
	cases = Case.objects.filter(user=user1)
	order = Order.objects.filter(sales_member=user1)
	context={
	'closed_won':closed_won,
	'closed_lost':closed_lost,
	'analysis':analysis,
	'perposal':perposal,
	'user1':user1,
	'lead':lead,
	'contacts':contacts,
	'cases':cases,
	'order':order,

	}
	return render(request, 'member-detail.html',context)

@login_required
def Order_total(request,id=''):
	user = request.user
	pr = Profile.objects.get(user=user).designation
	p = Order.objects.filter(sales_member=user)
	if user.is_superuser:
		return HttpResponse("You are Not Allowed ..!")
	else:
		if pr == 'Dispatch Team':
			return HttpResponse("You are Not Allowed ..!")
		if pr == "Sales Team":
			if id:
				n = len(id)
				a = int(id[:n-1])
				print(int(id[1]))
				if int(id[-1])==0:
					Order.objects.filter(order_id=a).update(stage="DELIVERED")
					return redirect('/ordered/items')
				if int(id[-1])==3:
					Order.objects.filter(order_id=a).update(status=False,stage="SENT FOR PRODUCTION")
					return redirect('/ordered/items')
			context = {
					'order': p
			}
			return render(request, 'total_order.html', context)


@login_required
def Order_place(request):
	products = Product.objects.all()
	lead = Lead.objects.all()
	sales_member = request.user
	pr = Profile.objects.get(user=sales_member).designation
	if sales_member.is_superuser:
		return HttpResponse("You are Not Allowed ..!")
	else:
		if pr == 'Dispatch Team':
			return HttpResponse("You are Not Allowed ..!")
		if pr == "Sales Team":
			if request.method == 'POST':
				#sales_member = request.user
				
				customer_id = request.POST.get('customer_name')
				customer_name = Lead.objects.get(lead_id=customer_id)
				customer_code = customer_name.code
				product_id = request.POST.get('product_name')
				product_name = Product.objects.get(id=product_id)
				product_code = product_name.product_code
				address = request.POST.get('f_address')
				hsn = product_name.HSN_Number
				#order_type = request.POST.get('order_type')
				quantity = request.POST.get('quantity')
				per_item_price = request.POST.get('per_item_price')
				packaging = request.POST.get('packaging')
				cat = request.POST.get('categories')
				#print(cat)
				cat1 = Category.objects.get(name=cat)
				gst = request.POST.get('gst')
				statutory = request.POST.get('statutory')
				solubility = request.POST.get('solubility')
				shipment_priority = request.POST.get('shipment_priority')
				shipment_preference = request.POST.get('shipment_preference')
				street = request.POST.get('street')
				city = request.POST.get('city')
				country = request.POST.get('customer_name')
				
				state = request.POST.get('state')
				postal_code = request.POST.get('postal_code')
				uom = request.POST.get('uom')
				# product 2
				product2 = request.POST.get('product_name2')
				if product2:
					#print("Hello")
					p = Product.objects.get(id=product2)
					product2 = p.product_name+', '+p.product_code
					code2 = p.product_code
				else:
					code2 = 0
					#print(product2)
				quantity2 = request.POST.get('quantity2')
				per_item_price2 = request.POST.get('per_item_price2')
				categories2 = request.POST.get('categories2')
				# product 3
				product3 = request.POST.get('product_name3')
				if product3:
					#print("Hello")
					p = Product.objects.get(id=product3)
					product3 = p.product_name+', '+p.product_code
					code3 = p.product_code
				else:
					code3 = 0
				quantity3 = request.POST.get('quantity3')
				per_item_price3 = request.POST.get('per_item_price3')
				categories3 = request.POST.get('categories3')
				# product 4
				product4 = request.POST.get('product_name4')
				if product4:
					#print("Hello")
					p = Product.objects.get(id=product4)
					product4 = p.product_name+', '+p.product_code
					code4 = p.product_code
				else:
					code4 = 0
				quantity4 = request.POST.get('quantity4')
				per_item_price4 = request.POST.get('per_item_price4')
				categories4 = request.POST.get('categories4')
				# product 5
				product5 = request.POST.get('product_name5')
				if product5:
					#print("Hello")
					p = Product.objects.get(id=product5)
					product5 = p.product_name+', '+p.product_code
					code5 = p.product_code
				else:
					code5 = 0
				quantity5 = request.POST.get('quantity5')
				per_item_price5 = request.POST.get('per_item_price5')
				categories5 = request.POST.get('categories5')
				# product 6
				product6 = request.POST.get('product_name6')
				if product6:
					#print("Hello")
					p = Product.objects.get(id=product6)
					product6 = p.product_name+', '+p.product_code
					code6 = p.product_code
				else:
					code6 = 0
				quantity6 = request.POST.get('quantity6')
				per_item_price6 = request.POST.get('per_item_price6')
				categories6 = request.POST.get('categories6')
				# product 7
				product7 = request.POST.get('product_name7')
				if product7:
					#print("Hello")
					p = Product.objects.get(id=product7)
					product7 = p.product_name+', '+p.product_code
					code7 = p.product_code
				else:
					code7 = 0
				quantity7 = request.POST.get('quantity7')
				per_item_price7 = request.POST.get('per_item_price7')
				categories7 = request.POST.get('categories7')
				# product 8
				product8 = request.POST.get('product_name8')
				if product8:
					#print("Hello")
					p = Product.objects.get(id=product8)
					product8 = p.product_name+', '+p.product_code
					code8 = p.product_code
				else:
					code8 = 0
				quantity8 = request.POST.get('quantity8')
				per_item_price8 = request.POST.get('per_item_price8')
				categories8 = request.POST.get('categories8')
				# product 9
				product9 = request.POST.get('product_name9')
				if product9:
					#print("Hello")
					p = Product.objects.get(id=product9)
					product9 = p.product_name+', '+p.product_code
					code9 = p.product_code
				else:
					code9 = 0
				quantity9 = request.POST.get('quantity9')
				per_item_price9 = request.POST.get('per_item_price9')
				categories9 = request.POST.get('categories9')
				# product 10
				product10 = request.POST.get('product_name10')
				if product10:
					#print("Hello")
					p = Product.objects.get(id=product10)
					product10 = p.product_name+', '+p.product_code
					code10 = p.product_code
				else:
					code10 = 0
				quantity10 = request.POST.get('quantity10')
				per_item_price10 = request.POST.get('per_item_price10')
				categories10 = request.POST.get('categories10')
				total_amount = int(quantity)*int(per_item_price)
				user = request.user
				if request.FILES:
					attachment = request.FILES['attachment']
					attachment1 = request.FILES['attachment1']
					attachment2 = request.FILES['attachment2']
					if attachment and attachment1 and attachment2:
						p = Order(order_lead=customer_name,sales_member=user,product_name=product_name,
							item_quantity=quantity,packaging=packaging,gst_number=gst,statutory=statutory,
							per_item_price=per_item_price,address=address,street=street,city=city,state=state,
							postal_code=postal_code,ship_country=country,total_amount=total_amount,
							shipment_priority=shipment_priority,shipment_mode=shipment_preference, 
							attachment=attachment,attachment1=attachment1,attachment2=attachment2,
							product_2=product2,code2 = code2, item_quantity2=quantity2,categories2=categories2,per_item_price2=per_item_price2,
							product_3=product3,code3 = code3, item_quantity3=quantity3,categories3=categories3,per_item_price3=per_item_price3,
							product_4=product4,code4 = code4, item_quantity4=quantity4,categories4=categories4,per_item_price4=per_item_price4,
							product_5=product5,code5 = code5, item_quantity5=quantity5,categories5=categories5,per_item_price5=per_item_price5,
							product_6=product6,code6 = code6, item_quantity6=quantity6,categories6=categories6,per_item_price6=per_item_price6,
							product_7=product7,code7 = code7, item_quantity7=quantity7,categories7=categories7,per_item_price7=per_item_price7,
							product_8=product8,code8 = code8, item_quantity8=quantity8,categories8=categories8,per_item_price8=per_item_price8,
							product_9=product9,code9 = code9, item_quantity9=quantity9,categories9=categories9,per_item_price9=per_item_price9,
							product_10=product10,code10 = code10, item_quantity10=quantity10,categories10=categories10,per_item_price10=per_item_price10)
					if attachment and attachment1:
						p = Order(order_lead=customer_name,sales_member=user,product_name=product_name,
							item_quantity=quantity,packaging=packaging,gst_number=gst,statutory=statutory,
							per_item_price=per_item_price,address=address,street=street,city=city,state=state,
							postal_code=postal_code,ship_country=country,total_amount=total_amount,
							shipment_priority=shipment_priority,shipment_mode=shipment_preference, 
							attachment=attachment,attachment1=attachment1,
							product_2=product2,code2 = code2, item_quantity2=quantity2,categories2=categories2,per_item_price2=per_item_price2,
							product_3=product3,code3 = code3, item_quantity3=quantity3,categories3=categories3,per_item_price3=per_item_price3,
							product_4=product4,code4 = code4, item_quantity4=quantity4,categories4=categories4,per_item_price4=per_item_price4,
							product_5=product5,code5 = code5, item_quantity5=quantity5,categories5=categories5,per_item_price5=per_item_price5,
							product_6=product6,code6 = code6, item_quantity6=quantity6,categories6=categories6,per_item_price6=per_item_price6,
							product_7=product7,code7 = code7, item_quantity7=quantity7,categories7=categories7,per_item_price7=per_item_price7,
							product_8=product8,code8 = code8, item_quantity8=quantity8,categories8=categories8,per_item_price8=per_item_price8,
							product_9=product9,code9 = code9, item_quantity9=quantity9,categories9=categories9,per_item_price9=per_item_price9,
							product_10=product10,code10 = code10, item_quantity10=quantity10,categories10=categories10,per_item_price10=per_item_price10)
					if attachment:
						p = Order(order_lead=customer_name,sales_member=user,product_name=product_name,
							item_quantity=quantity,packaging=packaging,gst_number=gst,statutory=statutory,
							per_item_price=per_item_price,address=address,street=street,city=city,state=state,
							postal_code=postal_code,ship_country=country,total_amount=total_amount,
							shipment_priority=shipment_priority,shipment_mode=shipment_preference, 
							attachment=attachment,
							product_2=product2, code2 = code2, item_quantity2=quantity2,categories2=categories2,per_item_price2=per_item_price2,
							product_3=product3, code3 = code3, item_quantity3=quantity3,categories3=categories3,per_item_price3=per_item_price3,
							product_4=product4, code4 = code4, item_quantity4=quantity4,categories4=categories4,per_item_price4=per_item_price4,
							product_5=product5, code5 = code5, item_quantity5=quantity5,categories5=categories5,per_item_price5=per_item_price5,
							product_6=product6, code6 = code6, item_quantity6=quantity6,categories6=categories6,per_item_price6=per_item_price6,
							product_7=product7, code7 = code7, item_quantity7=quantity7,categories7=categories7,per_item_price7=per_item_price7,
							product_8=product8, code8 = code8, item_quantity8=quantity8,categories8=categories8,per_item_price8=per_item_price8,
							product_9=product9, code9 = code9, item_quantity9=quantity9,categories9=categories9,per_item_price9=per_item_price9,
							product_10=product10, code10 = code10, item_quantity10=quantity10,categories10=categories10,per_item_price10=per_item_price10)
				else:
					p = Order(order_lead=customer_name,sales_member=user,product_name=product_name,
						item_quantity=quantity,packaging=packaging,gst_number=gst,statutory=statutory,
						per_item_price=per_item_price,address=address,street=street,city=city,state=state,
						postal_code=postal_code,ship_country=country,total_amount=total_amount,
						shipment_priority=shipment_priority,shipment_mode=shipment_preference,
						product_2=product2,code2 = code2,item_quantity2=quantity2,categories2=categories2,per_item_price2=per_item_price2,
							product_3=product3,code3 = code3,item_quantity3=quantity3,categories3=categories3,per_item_price3=per_item_price3,
							product_4=product4,code4 = code4,item_quantity4=quantity4,categories4=categories4,per_item_price4=per_item_price4,
							product_5=product5,code5 = code5,item_quantity5=quantity5,categories5=categories5,per_item_price5=per_item_price5,
							product_6=product6,code6 = code6,item_quantity6=quantity6,categories6=categories6,per_item_price6=per_item_price6,
							product_7=product7,code7 = code7,item_quantity7=quantity7,categories7=categories7,per_item_price7=per_item_price7,
							product_8=product8,code8 = code8,item_quantity8=quantity8,categories8=categories8,per_item_price8=per_item_price8,
							product_9=product9,code9 = code9,item_quantity9=quantity9,categories9=categories9,per_item_price9=per_item_price9,
							product_10=product10,code10 = code10,item_quantity10=quantity10,categories10=categories10,per_item_price10=per_item_price10)
					p.save()
					p.categories.add(cat1)
				return redirect('/ordered/items')
					
			else:
				return render(request, 'order_form.html',{"products":products,"lead":lead})
			return render(request, 'order_form.html',{"products":products,"lead":lead})



@login_required
def sample_total(request,id=''):
	user = request.user
	pr = Profile.objects.get(user=user).designation
	q = Sample.objects.filter(sales_member=user)
	if user.is_superuser:
		return HttpResponse("You are Not Allowed ..!")
	else:
		if pr == 'Dispatch Team':
			return HttpResponse("You are Not Allowed ..!")
		if pr == 'Sales Team':
		    if id:
		        n = len(id)
		        a = int(id[:n-1])
		        #print(int(id[1]))
		        if int(id[-1])==0:
		            Sample.objects.filter(id=a).update(stage="DELIVERED")
		            return redirect('/sample/items')
		        if int(id[-1])==3:
		            Sample.objects.filter(id=a).update(status=False,stage="SENT FOR PRODUCTION")
		            return redirect('/sample/items')
		    context = {
		            'sample': q
		    }
		    return render(request, 'total_sample.html', context)
@login_required
def sample_place(request):
	products = Product.objects.all()
	lead = Lead.objects.all()
	sales_member = request.user
	pr = Profile.objects.get(user=sales_member).designation
	if sales_member.is_superuser:
		return HttpResponse("You are Not Allowed ..!")
	else:
		if pr == 'Dispatch Team':
			return HttpResponse("You are Not Allowed ..!")
		if pr == 'Sales Team':
			if request.method == 'POST':
				
				customer_id = request.POST.get('customer_name')
				customer_name = Lead.objects.get(lead_id=customer_id)
				customer_code = customer_name.code
				product_id = request.POST.get('product_name')
				product_name = Product.objects.get(id=product_id)
				#product_code = product_name.product_code
				address = request.POST.get('f_address')
				#hsn = product_name.HSN_Number
				#order_type = request.POST.get('order_type')
				quantity = request.POST.get('quantity')
				per_item_price = request.POST.get('per_item_price')
				packaging = request.POST.get('packaging')
				#cat = request.POST.get('categories')
				# cat1 = Category.objects.get(name=cat)
				gst = request.POST.get('gst')
				statutory = request.POST.get('statutory')
				solubility = request.POST.get('solubility')
				shipment_priority = request.POST.get('shipment_priority')
				shipment_preference = request.POST.get('shipment_preference')
				street = request.POST.get('street')
				city = request.POST.get('city')
				country = request.POST.get('customer_name')

				state = request.POST.get('state')
				postal_code = request.POST.get('postal_code')
				uom = request.POST.get('uom')
				# sample 2
				sample2 = request.POST.get('product2_name')
				if sample2:
					p = Product.objects.get(id=sample2)
					sample2 = p.product_name+', '+p.product_code
					code2 = p.product_code
				else:
					code2 = 0
				quantity2 = request.POST.get('quantity2')
				per_item_price2 = request.POST.get('per_item_price2')
				packaging2 = request.POST.get('packaging2')
				# sample 3
				sample3 = request.POST.get('product3_name')
				if sample3:
					p = Product.objects.get(id=sample3)
					sample3 = p.product_name+', '+p.product_code
					code3 = p.product_code
				else:
					code3 = 0
				quantity3 = request.POST.get('quantity3')
				per_item_price3 = request.POST.get('per_item_price3')
				packaging3 = request.POST.get('packaging3')
				# sample 4
				sample4 = request.POST.get('product4_name')
				if sample4:
					p = Product.objects.get(id=sample4)
					sample4 = p.product_name+', '+p.product_code
					code4 = p.product_code
				else:
					code4 = 0
				quantity4 = request.POST.get('quantity4')
				per_item_price4 = request.POST.get('per_item_price4')
				packaging4 = request.POST.get('packaging4')
				# sample 5
				sample5 = request.POST.get('product5_name')
				if sample5:
					p = Product.objects.get(id=sample5)
					sample5 = p.product_name+', '+p.product_code
					code5 = p.product_code
				else:
					code5 = 0
				quantity5 = request.POST.get('quantity5')
				per_item_price5 = request.POST.get('per_item_price5')
				packaging5 = request.POST.get('packaging5')
				# sample 6
				sample6 = request.POST.get('product6_name')
				if sample6:
					p = Product.objects.get(id=sample6)
					sample6 = p.product_name+', '+p.product_code
					code6 = p.product_code
				else:
					code6 = 0
				quantity6 = request.POST.get('quantity6')
				per_item_price6 = request.POST.get('per_item_price6')
				packaging6 = request.POST.get('packaging6')
				# sample 7
				sample7 = request.POST.get('product7_name')
				if sample7:
					p = Product.objects.get(id=sample7)
					sample7 = p.product_name+', '+p.product_code
					code7 = p.product_code
				else:
					code7 = 0
				quantity7 = request.POST.get('quantity7')
				per_item_price7 = request.POST.get('per_item_price7')
				packaging7 = request.POST.get('packaging7')
				# sample 8
				sample8 = request.POST.get('product8_name')
				if sample8:
					p = Product.objects.get(id=sample8)
					sample8 = p.product_name+', '+p.product_code
					code8 = p.product_code
				else:
					code8 = 0
				quantity8 = request.POST.get('quantity8')
				per_item_price8 = request.POST.get('per_item_price8')
				packaging8 = request.POST.get('packaging8')
				# sample 9
				sample9 = request.POST.get('product9_name')
				if sample9:
					p = Product.objects.get(id=sample9)
					sample9 = p.product_name+', '+p.product_code
					code9 = p.product_code
				else:
					code9 = 0
				quantity9 = request.POST.get('quantity9')
				per_item_price9 = request.POST.get('per_item_price9')
				packaging9 = request.POST.get('packaging9')
				# sample 10
				sample10 = request.POST.get('product10_name')
				if sample10:
					p = Product.objects.get(id=sample10)
					sample10 = p.product_name+', '+p.product_code
					code10 = p.product_code
				else:
					code10 = 0
				quantity10 = request.POST.get('quantity10')
				per_item_price10 = request.POST.get('per_item_price10')
				packaging10 = request.POST.get('packaging10')
				total_amount = int(quantity)*int(per_item_price)
				if quantity2 and per_item_price2:
					total_amount = total_amount + int(quantity2)*int(per_item_price2)
				if quantity3 and per_item_price3:
					total_amount = total_amount + int(quantity3)*int(per_item_price3)
				if quantity4 and per_item_price4:
					total_amount = total_amount + int(quantity4)*int(per_item_price4)
				if quantity5 and per_item_price5:
					total_amount = total_amount + int(quantity5)*int(per_item_price5)
				if quantity6 and per_item_price6:
					total_amount = total_amount + int(quantity6)*int(per_item_price6)
				if quantity7 and per_item_price7:
					total_amount = total_amount + int(quantity7)*int(per_item_price7)
				if quantity8 and per_item_price8:
					total_amount = total_amount + int(quantity8)*int(per_item_price8)
				if quantity9 and per_item_price9:
					total_amount = total_amount + int(quantity9)*int(per_item_price9)
				if quantity10 and per_item_price10:
					total_amount = total_amount + int(quantity10)*int(per_item_price10)

				user = request.user
				q = Sample(sample_lead=customer_name,sales_member=user,sample_name=product_name,
				    item_quantity=quantity,gst_number=gst,statutory=statutory,
				    per_item_price=per_item_price,address=address,street=street,city=city,state=state,
				    postal_code=postal_code,ship_country=country,total_amount=total_amount,
				    shipment_priority=shipment_priority,shipment_mode=shipment_preference,
				    sample_2=sample2,code2=code2, item_quantity2=quantity2,packaging2=packaging2,per_item_price2=per_item_price2,
				    sample_3=sample3,code3=code3,item_quantity3=quantity3,packaging3=packaging3,per_item_price3=per_item_price3,
				    sample_4=sample4,code4=code4,item_quantity4=quantity4,packaging4=packaging4,per_item_price4=per_item_price4,
				    sample_5=sample5,code5=code5,item_quantity5=quantity5,packaging5=packaging5,per_item_price5=per_item_price5,
				    sample_6=sample6,code6=code6,item_quantity6=quantity6,packaging6=packaging6,per_item_price6=per_item_price6,
				    sample_7=sample7,code7=code7,item_quantity7=quantity7,packaging7=packaging7,per_item_price7=per_item_price7,
				    sample_8=sample8,code8=code8,item_quantity8=quantity8,packaging8=packaging8,per_item_price8=per_item_price8,
				    sample_9=sample9,code9=code9,item_quantity9=quantity9,packaging9=packaging9,per_item_price9=per_item_price9,
				    sample_10=sample10,code10=code10,item_quantity10=quantity10,packaging10=packaging10,per_item_price10=per_item_price10)
				q.save()
		        # q.categories.add(cat)
				return redirect('/sample/items')
			else:
				return render(request, 'sample_form.html',{"products":products,"lead":lead})
			return render(request, 'sample_form.html',{"products":products,"lead":lead})



def Item_list(request):
	return render(request, 'order.html')

def SelectOrder(request):
	return render(request, 'selectOrder.html')

def orderAddress(request):
	return render(request, 'order_address.html')

def Order1(request):
	#return render(request,'example.html')
	products = Product.objects.all()
	hsn = products[0].HSN_Number
	return render(request,'mainorder.html',{"products":products,"hsn":hsn})

class ProductSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	#print(queryset)
	serializer_class = ProductSerializer



@api_view(['GET', 'POST'])
def MeetingView(request):
	if request.method == "GET":
		meetings = Meeting.objects.filter(date__month__gte=now.month)
		serializer = MeetingSerializer(meetings, many=True)
		return Response(serializer.data)

	elif request.method == "POST":
		serializer = MeetingSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OpprtunityStages(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        a = list()
        a.append(Order.objects.filter(stage="APPROVAL").count())
        a.append(Order.objects.filter(stage="APPROVED").count())
        a.append(Order.objects.filter(stage="DELIVERED").count())
        a.append(Order.objects.filter(stage="REJECTED").count())
        a.append(Order.objects.filter(stage="ORDER DISPATCHED").count())
        data = {
            "list":a
        }
        return JsonResponse(data)


class LeadsStages(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	
	def get(self,request):
		user = request.user
		a = list()
		a.append(Lead.objects.filter(source="call").count())
		a.append(Lead.objects.filter(source="email").count())
		a.append(Lead.objects.filter(source="existing customer").count())
		a.append(Lead.objects.filter(source="partner").count())
		a.append(Lead.objects.filter(source="public relations").count())
		a.append(Lead.objects.filter(source="compaign").count())
		a.append(Lead.objects.filter(source="other").count())
		data = {
			"list":a
		}
		return JsonResponse(data)




def feedback_list(request):
	user = request.user
	if user.is_superuser:
		feedback = Feedback.objects.all()
		return render(request,'feedback_admin.html',{"feedback":feedback})
	else:
		feedback = Feedback.objects.filter(user=user)
		return render(request,'feedback_list.html',{'feedback':feedback})

def feedback_information(request,id):
	user = request.user
	feedback = Feedback.objects.get(feedback_id=id)
	if user.is_superuser:
		return render(request,"admin_feedback_information.html",{"feedback":feedback})
	else:
		return render(request,'feedback_information.html',{"feedback":feedback})


class Sales_Lead(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self,request):
		a = request.GET.get("name")
		if a:
			#print(a)
			user = User.objects.get(username=a)
		else:
			user = request.user
		a = list()
		a.append(Lead.objects.filter(user=user, source="call").count())
		a.append(Lead.objects.filter(user=user, source="email").count())
		a.append(Lead.objects.filter(user=user, source="existing customer").count())
		a.append(Lead.objects.filter(user=user, source="partner").count())
		a.append(Lead.objects.filter(user=user, source="public relations").count())
		a.append(Lead.objects.filter(user=user, source="compaign").count())
		a.append(Lead.objects.filter(user=user,source="other").count())
		data = {
			"list":a
		}
		return JsonResponse(data)


def import_contact(request):
	if request.method == "POST":
		form = UploadFileForm(request.POST,request.FILES)
		def choice_func(row):

			created_by = User.objects.filter(username=row[0])[0]
			#print(created_by)
			row[0]= created_by
			return row
		if form.is_valid():
			#print("Hello")
			request.FILES['file'].save_book_to_database(
				models=[Contact,],
				initializers=[choice_func,],
				mapdicts = [
				['created_by','first_name','last_name','email','phone','description'],
			]
				)
			return HttpResponse("File Uploaded")
		else:
			return HttpResponseBadRequest()
	else:
		form = UploadFileForm()
	return render(request,'contact_upload.html',{
			'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload sample-data.xls:'
		})


def taskpost(request):
	b = request.GET.get('start_date')
	title = request.GET.get('title')
	u = request.GET.get('user')
	e = request.GET.get('end_date')
	b = datetime.strptime(b, "%Y-%m-%d").date()
	end_date = datetime.strptime(e, "%Y-%m-%d").date()
	user = User.objects.get(username=u)
	p = Task(title=title,start_date=b,end_date=end_date,user=user)
	a = p.save()
	print(a)
	return JsonResponse({"data":True})

def meetingpost(request):
	b = request.GET.get('date')
	title = request.GET.get('name')
	e = request.GET.get('time')
	b = datetime.strptime(b, "%Y-%m-%d").date()
	time = datetime.strptime(e, "%H:%M")
	p = Meeting(name=title,date=b,time=time)
	a = p.save()
	print(title)
	return JsonResponse({"data":True})

def meeting_list(request):
	meeting = Meeting.objects.filter(date__gte=now.date())
	t = []
	s_d = []
	e_d = []
	for i in meeting:
		s_d.append(i.date)
		e_d.append(i.name)
		t.append(i.time)
	return JsonResponse({"date":s_d,"title":e_d,"time":t})


def task_list(request):
	user = request.user
	task = Task.objects.filter(user=user,end_date__gte=now.date())
	t = []
	s_d = []
	e_d = []
	for i in task:
		s_d.append(i.start_date)
		e_d.append(i.end_date)
		t.append(i.title)
	return JsonResponse({"start_date":s_d,"end_date":e_d,"title":t})

def salestask(request):
	b = request.GET.get('start_date')
	title = request.GET.get('title')
	e = request.GET.get('end_date')
	b = datetime.strptime(b, "%Y-%m-%d").date()
	end_date = datetime.strptime(e, "%Y-%m-%d").date()
	user = request.user
	p = Task(title=title,start_date=b,end_date=end_date,user=user)
	a = p.save()
	print(a)
	return JsonResponse({"data":True})


def salestask_list(request):
	user = request.user
	task = Task.objects.filter(user=user,end_date__gte=now.date())
	t = []
	s_d = []
	e_d = []
	for i in task:
		s_d.append(i.start_date)
		e_d.append(i.end_date)
		t.append(i.title)
	return JsonResponse({"start_date":s_d,"end_date":e_d,"title":t})

def visittask_list(request):
	user = request.GET.get("user")
	user = User.objects.get(username=user)
	task = Task.objects.filter(user=user,end_date__lte=now.date())
	t = []
	s_d = []
	e_d = []
	for i in task:
		s_d.append(i.start_date)
		e_d.append(i.end_date)
		t.append(i.title)
	return JsonResponse({"start_date":s_d,"end_date":e_d,"title":t})


def Sales_persons(request):
	persons = User.objects.filter(is_staff=False,is_superuser=False)
	profiles = Profile.objects.all()
	context = {
		"persons":persons,
		"profiles":profiles,
	}
	return render(request,'sales-members.html',context)

def example(request):
	return render(request,'admin-opportunity.html')

def change_opportunity(request,id):
	
	opportunity = Opprtunity.objects.get(id=id)
	#print(request.GET.get("name"))
	form = OpportunityForm(request.POST)
	lead = form['lead'].value()
	
	#prform['name'].value())
	#print(opportunity.name)
	return render(request,'edit_opprtunity.html',{'opportunity':opportunity})

def edit_lead(request,id):
	lead = Lead.objects.filter(lead_id=id)[0]
	#print(request.GET.get("name"))
	form = LeadUpdateForm(request.POST)
	status = form['status'].value()
	phone = form['phone'].value()
	email = form['email'].value()
	description = form['description'].value()
	#print(status,phone,email,description)
	#l = Lead.objects.filter(lead_id=id).update(status=status,phone=phone,email=email,description=description)
	
	return render(request,'edit_lead.html',{"lead":lead})
def import_lead(request):
	if request.method == "POST":
		form = UploadFileForm(request.POST, request.FILES)
		def choice_func(row):
			#print(row)
			user = User.objects.filter(username=row[0])[0]
			row[0] = user
			return row
		if form.is_valid():
			request.FILES['file'].save_book_to_database(
				models = [Lead,],
				initializers = [choice_func,],
				mapdicts = [
				# ['user','contacts','code','first_name','last_name','lead_company','status','source','email','phone'
				# ,'website','address','street','city','state','postal_code','country','description'],
				['user','code','lead_company','phone','email']
				]
				)
			return HttpResponse("File Uploaded")
		else:
			return HttpResponseBadRequest()
	else:
		form = UploadFileForm()
	return render(request,'contact_upload.html',{
			'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload sample-data.xls:'
		})



def import_order(request):
	if request.method == "POST":
		form = UploadFileForm(request.POST, request.FILES)
		def choice_func(row):
			#print(row[2])
			lead = Lead.objects.filter(lead_company=row[0])[0]
			#print(lead)
			user = User.objects.filter(username=row[1])[0]
			#print(user)
			#product = Lead.objects.filter(code=row[2])[0]
			#print(product)
			row[1]=user
			row[0] = lead
			#row[2] = product
			return row
		if form.is_valid():
			request.FILES['file'].save_book_to_database(
				models = [Order,],
				initializers = [choice_func,],
				mapdicts = [
				# ['user','contacts','code','first_name','last_name','lead_company','status','source','email','phone'
				# ,'website','address','street','city','state','postal_code','country','description'],
				['order_lead','sales_member','code','item_name','item_quantity','hsn','order_type',
				'uom','per_item_price',
				'shipment_mode','total_amount']
				]
				)
			return HttpResponse("File Uploaded")
		else:
			return HttpResponseBadRequest()
	else:
		form = UploadFileForm()
	return render(request,'contact_upload.html',{
			'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload sample-data.xls:'
		})

def import_payment(request):
	if request.method == "POST":
		form = UploadFileForm(request.POST, request.FILES)
		def choice_func(row):
			#print(row[2])
			created_by = User.objects.filter(username=row[0])[0]
			#print(lead)
			lead = Lead.objects.filter(code=row[1])[0]
			order_name = Order.objects.filter(order_lead=lead,sales_member=created_by,order_name=row[2])[0]
			
			#print(user)
			#product = Lead.objects.filter(code=row[2])[0]
			#print(product)
			row[0]=created_by
			row[1] = lead
			row[2] = order_name
			#row[2] = product
			return row
		if form.is_valid():
			request.FILES['file'].save_book_to_database(
				models = [Payment,],
				initializers = [choice_func,],
				mapdicts = [
				# ['user','contacts','code','first_name','last_name','lead_company','status','source','email','phone'
				# ,'website','address','street','city','state','postal_code','country','description'],
				['created_by','leads','order_name','invoice_id','transaction_id','product_hsn_code',
				'payment_date','payment_amount','total_amount','item_quantity','categories']
				]
				)
			return HttpResponse("File Uploaded")
		else:
			return HttpResponseBadRequest()
	else:
		form = UploadFileForm()
	return render(request,'contact_upload.html',{
			'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload sample-data.xls:'
		})

class my_dictionary(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 


@login_required
def sales_report(request):
	country = request.GET.get('country')
	if country:
		order = Payment.objects.filter(leads__country__contains=country)
	else:
		order = Payment.objects.all()
	ordered = sorted(order, key=operator.attrgetter('payment_date'))
	data = []
	amount = []
	dict_obj = my_dictionary()
	for i in ordered:
		data.append(i.payment_date)
		amount.append(i.pay_amount)
		
	return JsonResponse({"result":data,"amount":amount})



def admin_opportunity(request):
	order = Order.objects.all()
	#print("hello")
	#print(opportunities)
	return render(request,'admin-opportunity.html',{"order":order})

def admin_lead(request):
	lead = Lead.objects.all()
	return render(request,'lead-admin.html',{"lead":lead})
    
def admin_contact(request):
	contacts = Contact.objects.all()
	return render(request,'admin-contact.html',{"contacts":contacts})
def admin_case(request):
	case = Case.objects.all()
	return render(request,'admin-case.html',{"case":case})
def admin_document(request):
	document = Document.objects.all()
	return render(request,'admin-document.html',{"document":document})
def admin_payment(request,id=''):
	payments = Payment.objects.all()
	print(payments)
	if id:
		n =len(id)
		a = int(id[:n-1])
		if int(id[-1])==0:
			p = Payment.objects.get(payment_id=a)
			paid = p.total_amount
			Payment.objects.filter(payment_id=a).update(status=True,pay_amount=paid)
			s = p.order_name.order_id
			Order.objects.filter(order_id=s).update(status=True)
			return redirect('/payment/admin')
		if int(id[-1])==1:
			p = Payment.objects.get(payment_id=a)
			paid = p.total_amount - p.due_amount
			Payment.objects.filter(payment_id=a).update(status=False,pay_amount=paid)
			s = p.order_name.order_id
			Order.objects.filter(order_id=s).update(status=False)
			return redirect('/payment/admin')
	return render(request,'admin-payment.html',{'payments':payments})

def user_payment(request, id=''):
	if id:
		n =len(id)
		a = int(id[:n-1])
		if int(id[-1])==0:
			p = Payment.objects.get(payment_id=a)
			paid = p.total_amount
			Payment.objects.filter(payment_id=a).update(status=True,pay_amount=paid)
			s = p.order_name.order_id
			Order.objects.filter(order_id=s).update(status=True)
			return redirect('/user/payment/list')
	user = request.user
	payments = Payment.objects.filter(created_by = user)
	return render(request,'user-payment.html',{'payments':payments})

def add_payment(request):
	form = PaymentForm(request.POST)
	if request.method=="POST":
		if request.FILES:
			form = PaymentForm(request.POST, request.FILES)
		else:
			form = PaymentForm(request.POST)
		if form.is_valid():
			order_id = form['order_name'].value()
			order = Order.objects.get(order_id=order_id)
			paid = form["pay_amount"].value()
			#print(paid)
			obj = form.save()
			obj.created_by = request.user
			amount = order.total_amount
			obj.due_amount = int(amount) - int(paid)
			if int(paid)==int(amount):
				obj.status = True
			#print(due_amount)
			obj.total_amount = amount
			obj.item_quantity = order.packaging
			obj.product_hsn_code = order.hsn
			obj.save()
			return redirect('/payment/admin')
	else:
		form = PaymentForm()
	return render(request,'add-payment.html',{"form":form})#'add-payment.html')

def user_add_payment(request):
	order = Performa.objects.all()
	lead = order
	if request.method=="POST":
		invoice_id = request.POST.get("invoice_id")
		transaction_id = request.POST.get("transaction_id")
		pay_amount = request.POST.get("pay_amount")
		customer_id = request.POST.get("customer_name")
		customer_name = Lead.objects.get(lead_id=customer_id)
		order_id = request.POST.get("order_name")
		#print(order_id)
		product_name = Performa.objects.get(id=order_id)
		#print(product_name)
		
		pay_date = request.POST.get("pay_date")
		categories = request.POST.get("categories")
		#print(order_id)
		created_by = request.user
		amount = product_name.total_amount
		due_amount = int(float(amount) - float(pay_amount))
		#item_quantity = product_name.item_quantity
		pay_amount = int(float(pay_amount))
		amount = int(float(amount))
		product_hsn_code = product_name.product_name.HSN_Number
		if float(pay_amount)==float(amount):
			status = True

		else:
			status = False

		if request.FILES:
			attachment = request.FILE['attachment']
		else:
			attachment = ''
		p = Payment(invoice_id=invoice_id,transaction_id=transaction_id,pay_amount=pay_amount,
			order_name=product_name,leads=customer_name,payment_date=pay_date,categories=categories,
			created_by=created_by,due_amount=due_amount,status=status,
			product_hsn_code=product_hsn_code,total_amount=amount)
		p.save()
		return redirect('/user/payment/list')
	else:
		return render(request,'user-add-payment.html',{"orders":order,"lead":lead})
	return render(request,'user-add-payment.html',{"orders":order,"lead":lead})
def pending_order(request,id=''):
	
	pending = Opprtunity.objects.filter(stage="APPROVAL")
	if id:
		n =len(id)
		a = int(id[:n-1])
		if int(id[-1])==1:
			Opprtunity.objects.filter(id=a).update(stage="APPROVAL APPROVED")
		if int(id[-1])==0:
			Opprtunity.objects.filter(id=a).update(stage="REJECTED")
		#print(pending)
	return render(request,'pending-order.html',{"pending":pending})


def add_product(request):
    user = request.user
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect("/add/product")
    else:
        form = ProductForm()
    profile = Profile.objects.get(user=user)
    context = {
                'form': form,
                'profile': profile,
    }
    return render(request,'add-product.html',context)
 
def order_confirmation(request,id=''):
	order = Order.objects.filter(stage="APPROVAL")
	sample = Sample.objects.filter(stage="APPROVAL")
	if id:
		n =len(id)
		a = int(id[:n-1])
		if int(id[-1])==1:
			Order.objects.filter(order_id=a).update(stage="APPROVED")
			return redirect('/order/confirmation')
		if int(id[-1])==0:
			Order.objects.filter(order_id=a).update(stage="REJECTED")
			return redirect('/order/confirmation')
		if int(id[-1])==3:
			Sample.objects.filter(id=a).update(stage="APPROVED")
			return redirect('/order/confirmation')
		if int(id[-1])==4:
			Sample.objects.filter(id=a).update(stage="REJECTED")
			return redirect('/order/confirmation')
	return render(request,'confirm_order.html',{"order":order,"sample":sample})





from django.http import HttpResponse
from django.views.generic import View

from .utils import render_to_pdf #created in step 4




# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         data = {
#              'today': datetime.date.today(), 
#              'amount': 39.99,
#             'customer_name': 'Cooper Mann',
#             'order_id': 1233434,
#         }
#         pdf = render_to_pdf('pdf/invoice.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')


# class GeneratePDF(View):
#     def get(self, request, *args, **kwargs):
#         template = get_template('invoice-quotation.html')
#         context = {
#             "invoice_id": 123,
#             "customer_name": "John Cooper",
#             "amount": 1399.99,
#             "today": "Today",
#         }
#         html = template.render(context)
#         pdf = render_to_pdf('invoice-quotation.html', context)
#         if pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             filename = "Invoice_%s.pdf" %("12341231")
#             content = "inline; filename='%s'" %(filename)
#             download = request.GET.get("download")
#             if download:
#                 content = "attachment; filename='%s'" %(filename)
#             response['Content-Disposition'] = content
#             return response
#         return HttpResponse("Not found")

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice-quotation.html')
        logo = PdfPhoto.objects.get()
        url = "static/assets/css/style-invoice.css"
        print(logo)
        context = {
        	"url":url,
        	"logo":logo,
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice-quotation.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


def p_q_list(request):
	user = request.user
	quotations = Quotation.objects.filter(user=user)
	performas = Performa.objects.filter(user=user)
	context = {
		"quotations":quotations,
		"performas":performas
	}
	return render(request,'porforma-quotation.html',context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def p_q_userlist(request):
	quotations = Quotation.objects.all()
	performa = Performa.objects.all()
	context = {
		"quotations":quotations,
		"performa":performa
	}
	return render(request,'proforma-quotation.html',context)

def pro_form(request, id=''):
	products = Product.objects.all()
	if id:
		values = Order.objects.get(order_id=id)
		if values.code2 != '0':
			code2 = values.code2
			p2_id = Product.objects.get(product_code=code2).id
		else:
			p2_id = 0

		if values.code3 != '0':
			code3 = values.code3
			p3_id = Product.objects.get(product_code=code3).id
		else:
			p3_id = 0

		if values.code4 != '0':
			code4 = values.code4
			p4_id = Product.objects.get(product_code=code4).id
		else:
			p4_id = 0

		if values.code5 != '0':
			code5 = values.code5
			p5_id = Product.objects.get(product_code=code5).id
		else:
			p5_id = 0

		if values.code6 != '0':
			code6 = values.code6
			p6_id = Product.objects.get(product_code=code6).id

		else:
			p6_id = 0

		if values.code7 != '0':
			code7 = values.code7
			p7_id = Product.objects.get(product_code=code7).id
		else:
			p7_id = 0

		if values.code8 != '0':
			code8 = values.code8
			p8_id = Product.objects.get(product_code=code8).id
		else:
			p8_id = 0

		if values.code9 != '0':
			code9 = values.code9
			p9_id = Product.objects.get(product_code=code9).id
		else:
			p9_id = 0

		if values.code10 != '0':
			code10 = values.code10
			p10_id = Product.objects.get(product_code=code10).id
		else:
			p10_id = 0

	else:
		values = 0
		p2_id = 0
		p3_id = 0
		p4_id = 0
		p5_id = 0
		p6_id = 0
		p7_id = 0
		p8_id = 0
		p9_id = 0
		p10_id = 0

	form = PerformaForm()
	if request.method == "POST":
		form = PerformaForm(request.POST)
		if form.is_valid():
			#print("Hello")
			quantity = form['quantity'].value()
			rate = form['per_item_price'].value()
			freight = form['freight'].value()
			gst_number = form['gst_number'].value()
			pan_number = form['pan_number'].value()
			ecc = form['ecc'].value()
			payment_terms = form['payment_terms'].value()
			delivere_terms = form['delivere_terms'].value()
			remarks = form['remarks'].value()
			insurance = form['insurance'].value()
			date = form['tentative_date'].value()
			
			product1_amount = int(quantity)*int(rate)
			customer_id = form['customer_name'].value()
			customer_name = Lead.objects.get(lead_id=customer_id)
			customer_code = customer_name.code
			customer_contact = form['customer_contact'].value()
			product_id = form['product_name'].value()
			product_name = Product.objects.get(id=product_id)
			quantity = form['quantity'].value()
			per_item_price = form['per_item_price'].value()
			# product 2
			product2 = form['product2'].value()
			code2 = form['code2'].value()
			quantity2 = form['quantity2'].value()
			per_item_price2 = form['per_item_price2'].value()
			# product 3
			product3 = form['product3'].value()
			code3 = form['code3'].value()
			quantity3 = form['quantity3'].value()
			per_item_price3 = form['per_item_price3'].value()
			# product 4
			product4 = form['product4'].value()
			code4 = form['code4'].value()
			quantity4 = form['quantity4'].value()
			per_item_price4 = form['per_item_price4'].value()
			# product 6
			product5 = form['product5'].value()
			code5 = form['code5'].value()
			quantity5 = form['quantity5'].value()
			per_item_price5 = form['per_item_price5'].value()
			# product 6
			product6 = form['product6'].value()
			code6 = form['code6'].value()
			quantity6 = form['quantity6'].value()
			per_item_price6 = form['per_item_price6'].value()
			# product 7
			product7 = form['product7'].value()
			code7 = form['code7'].value()
			quantity7 = form['quantity7'].value()
			per_item_price7 = form['per_item_price7'].value()
			# product 8
			product8 = form['product8'].value()
			code8 = form['code8'].value()
			quantity8 = form['quantity8'].value()
			per_item_price8 = form['per_item_price8'].value()
			# product 9
			product9 = form['product9'].value()
			code9 = form['code9'].value()
			quantity9 = form['quantity9'].value()
			per_item_price9 = form['per_item_price9'].value()
			# product 10
			product10 = form['product10'].value()
			code10 = form['code10'].value()
			quantity10 = form['quantity10'].value()
			per_item_price10 = form['per_item_price10'].value()
			bank_id = form['bank_name'].value()
			bank_name = BankDetails.objects.get(id=bank_id)

			if per_item_price and quantity2 and product2:
				product2 = Product.objects.get(id=product2)
				product2_amount = int(per_item_price2) * int(quantity2)
				product1_amount += product2_amount
			if per_item_price3 and quantity3 and product3:
				product3 = Product.objects.get(id=product3)
				product3_amount = int(per_item_price3) * int(quantity3)
				product1_amount += product3_amount
			if per_item_price4 and quantity4 and product4:
				product4 = Product.objects.get(id=product4)
				product4_amount = int(per_item_price4) * int(quantity4)
				product1_amount += product4_amount
			if per_item_price5 and quantity5 and product5:
				product5 = Product.objects.get(id=product5)
				product5_amount = int(per_item_price5) * int(quantity5)
				product1_amount += product5_amount
			if per_item_price6 and quantity6 and product6:
				product6 = Product.objects.get(id=product6)
				product6_amount = int(per_item_price6) * int(quantity6)
				product1_amount += product6_amount
			if per_item_price7 and quantity7 and product7:
				product7 = Product.objects.get(id=product7)
				product7_amount = int(per_item_price7) * int(quantity7)
				product1_amount += product7_amount
			if per_item_price8 and quantity8 and product8:
				product8 = Product.objects.get(id=product_id8)
				product8_amount = int(per_item_price8) * int(quantity8)
				product1_amount += product8_amount
			if per_item_price9 and quantity9 and product9:
				product9 = Product.objects.get(id=product_id9)
				product9_amount = int(per_item_price9) * int(quantity9)
				product1_amount += product9_amount
			if per_item_price10 and quantity10 and product10:
				product1 = Product.objects.get(id=product10)
				product10_amount = int(per_item_price1) * int(quantity10)
				product1_amount += product10_amount
			if insurance == True:
				product1_amount = product1_amount + product1_amount*insurance #0.003 replaced with insurance
			product1_amount = int(freight) + product1_amount 
			igst = product1_amount*0.18
			product1_amount =  product1_amount + igst
			
			igsst_cost = igst
			user = request.user
			total_amount = product1_amount
			p = Performa(customer_name = customer_name, customer_contact=customer_contact,
				product_name=product_name,quantity=quantity,per_item_price=per_item_price,
				user=user,igsst_cost=igsst_cost,total_amount=total_amount,freight=freight,tentative_date=date,
				pan_number=pan_number,gst_number=gst_number,ecc=ecc,payment_terms=payment_terms,
				delivere_terms=delivere_terms,remarks=remarks,insurance=insurance,bank_name=bank_name,
				product2=product2,code2=code2,quantity2=quantity2,per_item_price2=per_item_price2,
				product3=product3,code3=code3,quantity3=quantity3,per_item_price3=per_item_price3,
				product4=product4,code4=code4,quantity4=quantity4,per_item_price4=per_item_price4,
				product5=product5,code5=code5,quantity5=quantity5,per_item_price5=per_item_price5,
				product6=product6,code6=code6,quantity6=quantity6,per_item_price6=per_item_price6,
				product7=product7,code7=code7,quantity7=quantity7,per_item_price7=per_item_price7,
				product8=product8,code8=code8,quantity8=quantity8,per_item_price8=per_item_price8,
				product9=product9,code9=code9,quantity9=quantity9,per_item_price9=per_item_price9,
				product10=product10,code10=code10,quantity10=quantity10,per_item_price10=per_item_price10,)
			p.save()
			Lead.objects.filter(code=customer_code).update(gst_number=gst_number)
			return redirect('/porforma_quotation/list')
	else:
		form = PerformaForm()
	context = {
				"form":form,
				"products":products,
				"values":values,
				'p2_id': p2_id,
				'p3_id': p3_id,
				'p4_id': p4_id,
				'p5_id': p5_id,
				'p6_id': p6_id,
				'p7_id': p7_id,
				'p8_id': p8_id,
				'p9_id': p9_id,
				'p10_id': p10_id,

	}
	return render(request,'proforma-form.html',context)

def quo_form(request, id=None):
	products = Product.objects.all()
	if id:
		values = Sample.objects.get(id=id)
		if values.code2 != '0':
			code2 = values.code2
			pq2_id = Product.objects.get(product_code=code2).id
		else:
			pq2_id = 0

		if values.code3 != '0':
			code3 = values.code3
			pq3_id = Product.objects.get(product_code=code3).id
		else:
			pq3_id = 0

		if values.code4 != '0':
			code4 = values.code4
			pq4_id = Product.objects.get(product_code=code4).id
		else:
			pq4_id = 0

		if values.code5 != '0':
			code5 = values.code5
			pq5_id = Product.objects.get(product_code=code5).id
		else:
			pq5_id = 0

		if values.code6 != '0':
			code6 = values.code6
			pq6_id = Product.objects.get(product_code=code6).id

		else:
			pq6_id = 0

		if values.code7 != '0':
			code7 = values.code7
			pq7_id = Product.objects.get(product_code=code7).id
		else:
			pq7_id = 0

		if values.code8 != '0':
			code8 = values.code8
			pq8_id = Product.objects.get(product_code=code8).id
		else:
			pq8_id = 0

		if values.code9 != '0':
			code9 = values.code9
			pq9_id = Product.objects.get(product_code=code9).id
		else:
			pq9_id = 0

		if values.code10 != '0':
			code10 = values.code10
			pq10_id = Product.objects.get(product_code=code10).id
		else:
			pq10_id = 0

	else:
		values = 0
		pq2_id = 0
		pq3_id = 0
		pq4_id = 0
		pq5_id = 0
		pq6_id = 0
		pq7_id = 0
		pq8_id = 0
		pq9_id = 0
		pq10_id = 0
	form = QuotationForm()
	#print("hello")
	if request.method == "POST":
		#print("Hello")
		form = QuotationForm(request.POST)
		if form.is_valid():
			user = request.user
			customer_id = form['customer_name'].value()
			customer_name = Lead.objects.get(lead_id=customer_id)
			customer_code = form['customer_code'].value()
			customer_address = form['address'].value()
			igst_code = form['igst'].value()
			payment_term = form['payment_term'].value()
			freight = form['freight'].value()
			delivery_term = form['delivery_term'].value()	
			lead_term = form['lead_term'].value()
			product1 = form['product_name'].value()
			product_name = Product.objects.get(id=product1)
			product_code = product_name.product_code		
			price_per_1kg = form['price_per_1kg'].value()
			price_per_5kg = form['price_per_5kg'].value()
			price_per_25kg = form['price_per_25kg'].value()
			price_per_50kg = form['price_per_50kg'].value()
			# product2
			product2 = form['product2'].value()
			code2 = form['code2'].value()
			price_per_1kg2 = form['price_per_1kg2'].value()
			price_per_5kg2 = form['price_per_5kg2'].value()
			price_per_25kg2 = form['price_per_25kg2'].value()
			price_per_50kg2 = form['price_per_50kg2'].value()
			# product 3
			product3 = form['product3'].value()
			code3 = form['code3'].value()
			price_per_1kg3 = form['price_per_1kg3'].value()
			price_per_5kg3 = form['price_per_5kg3'].value()
			price_per_25kg3 = form['price_per_25kg3'].value()
			price_per_50kg3 = form['price_per_50kg3'].value()
			# product 4
			product4 = form['product4'].value()
			code4 = form['code4'].value()
			price_per_1kg4 = form['price_per_1kg4'].value()
			price_per_5kg4 = form['price_per_5kg4'].value()
			price_per_25kg4 = form['price_per_25kg4'].value()
			price_per_50kg4 = form['price_per_50kg4'].value()
			# product 6
			product5 = form['product5'].value()
			code5 = form['code5'].value()
			price_per_1kg5 = form['price_per_1kg5'].value()
			price_per_5kg5 = form['price_per_5kg5'].value()
			price_per_25kg5 = form['price_per_25kg5'].value()
			price_per_50kg5 = form['price_per_50kg5'].value()
			# product 6
			product6 = form['product6'].value()
			code6 = form['code6'].value()
			price_per_1kg6 = form['price_per_1kg6'].value()
			price_per_5kg6 = form['price_per_5kg6'].value()
			price_per_25kg6 = form['price_per_25kg6'].value()
			price_per_50kg6 = form['price_per_50kg6'].value()
			# product 7
			product7 = form['product7'].value()
			code7 = form['code7'].value()
			price_per_1kg7 = form['price_per_1kg7'].value()
			price_per_5kg7 = form['price_per_5kg7'].value()
			price_per_25kg7 = form['price_per_25kg7'].value()
			price_per_50kg7 = form['price_per_50kg7'].value()
			# product 8
			product8 = form['product8'].value()
			code8 = form['code8'].value()
			price_per_1kg8 = form['price_per_1kg8'].value()
			price_per_5kg8 = form['price_per_5kg8'].value()
			price_per_25kg8 = form['price_per_25kg8'].value()
			price_per_50kg8 = form['price_per_50kg8'].value()
			# product 9
			product9 = form['product9'].value()
			code9 = form['code9'].value()
			price_per_1kg9 = form['price_per_1kg9'].value()
			price_per_5kg9 = form['price_per_5kg9'].value()
			price_per_25kg9 = form['price_per_25kg9'].value()
			price_per_50kg9 = form['price_per_50kg9'].value()
			# product 10
			product10 = form['product10'].value()
			code10 = form['code10'].value()
			price_per_1kg10 = form['price_per_1kg10'].value()
			price_per_5kg10 = form['price_per_5kg10'].value()
			price_per_25kg10 = form['price_per_25kg10'].value()
			price_per_50kg10 = form['price_per_50kg10'].value()

			product1_amount = int(price_per_1kg)
			if price_per_5kg:
				product1_amount = product1_amount + int(price_per_5kg) 
			if price_per_25kg:
				product1_amount = product1_amount + int(price_per_25kg)
			if price_per_50kg:
				product1_amount = product1_amount + int(price_per_50kg)

			if price_per_1kg2 and product2:
				product2 = Product.objects.get(id=product2)
				product2_amount = int(price_per_1kg2) + int(price_per_5kg2) + int(price_per_25kg2) + int(price_per_50kg2)
				product1_amount += product2_amount
			if price_per_1kg3 and product3:
				product3 = Product.objects.get(id=product3)
				product3_amount = int(price_per_1kg3) + int(price_per_5kg3) + int(price_per_25kg3) + int(price_per_50kg3)
				product1_amount += product3_amount
			if price_per_1kg4 and product4:
				product4 = Product.objects.get(id=product4)
				product4_amount = int(price_per_1kg4) + int(price_per_5kg4) + int(price_per_25kg4) + int(price_per_50kg4)
				product1_amount += product4_amount
			if price_per_1kg5 and product5:
				product5 = Product.objects.get(id=product5)
				product5_amount =int(price_per_1kg5) +int(price_per_5kg5) +int(price_per_25kg5) +int(price_per_50kg5)
				product1_amount += product5_amount
			if price_per_1kg6 and product6:
				product6 = Product.objects.get(id=product6)
				product6_amount =int(price_per_1kg) +int(price_per_5kg6) +int(price_per_25kg6) +int(price_per_50kg6)
				product1_amount += product6_amount
			if price_per_1kg7 and product_id7:
				product7 = Product.objects.get(id=product7)
				product7_amount =int(price_per_1kg7) +int(price_per_5kg7) +int(price_per_25kg7) +int(price_per_50kg7)
				product1_amount += product7_amount
			if price_per_1kg8 and product8:
				product8 = Product.objects.get(id=product8)
				product8_amount =int(price_per_1kg8) +int(price_per_5kg8) +int(price_per_25kg8) +int(price_per_50kg8)
				product1_amount += product8_amount
			if price_per_1kg9 and product9:
				product9 = Product.objects.get(id=product9)
				product9_amount =int(price_per_1kg9) +int(price_per_5kg9) +int(price_per_25kg9) +int(price_per_50kg9)
				product1_amount += product9_amount
			if price_per_1kg10 and product10:
				product1 = Product.objects.get(id=product10)
				product10_amount =int(price_per_1kg10) + int(price_per_5kg10) + int(price_per_25kg10) + int(price_per_50kg10)
				product1_amount += product10_amount
			
			total_amount = int(product1_amount)
			print(total_amount)
			p = Quotation(user=user,customer_name=customer_name,customer_code=customer_code,
				igst=igst_code,payment_term=payment_term,delivery_term=delivery_term,lead_term=lead_term,
				freight=freight,product_name=product_name,product_code=product_code,price_per_1kg=price_per_1kg,
				price_per_5kg=price_per_5kg,price_per_25kg=price_per_25kg,price_per_50kg=price_per_50kg,
				product2=product2,price_per_1kg2=price_per_1kg2,price_per_5kg2=price_per_5kg2,price_per_25kg2=price_per_25kg2,price_per_50kg2=price_per_50kg2,
				product3=product3,price_per_1kg3=price_per_1kg3,price_per_5kg3=price_per_5kg3,price_per_25kg3=price_per_25kg3,price_per_50kg3=price_per_50kg3,
				product4=product4,price_per_1kg4=price_per_1kg4,price_per_5kg4=price_per_5kg4,price_per_25kg4=price_per_25kg4,price_per_50kg4=price_per_50kg4,
				product5=product5,price_per_1kg5=price_per_1kg5,price_per_5kg5=price_per_5kg5,price_per_25kg5=price_per_25kg5,price_per_50kg5=price_per_50kg5,
				product6=product6,price_per_1kg6=price_per_1kg6,price_per_5kg6=price_per_5kg6,price_per_25kg6=price_per_25kg6,price_per_50kg6=price_per_50kg6,
				product7=product7,price_per_1kg7=price_per_1kg7,price_per_5kg7=price_per_5kg7,price_per_25kg7=price_per_25kg7,price_per_50kg7=price_per_50kg7,
				product8=product8,price_per_1kg8=price_per_1kg8,price_per_5kg8=price_per_5kg8,price_per_25kg8=price_per_25kg8,price_per_50kg8=price_per_50kg8,
				product9=product9,price_per_1kg9=price_per_1kg9,price_per_5kg9=price_per_5kg9,price_per_25kg9=price_per_25kg9,price_per_50kg9=price_per_50kg9,
				product10=product10,price_per_1kg10=price_per_1kg10,price_per_5kg10=price_per_5kg10,price_per_25kg10=price_per_25kg10,price_per_50kg10=price_per_50kg10,)
				
			p.save()
			return redirect('/porforma_quotation/list')

	else:
		form = QuotationForm()
	context = {
				"form":form,
				"products":products,
				"values":values,
				'pq2_id': pq2_id,
				'pq3_id': pq3_id,
				'pq4_id': pq4_id,
				'pq5_id': pq5_id,
				'pq6_id': pq6_id,
				'pq7_id': pq7_id,
				'pq8_id': pq8_id,
				'pq9_id': pq9_id,
				'pq10_id': pq10_id,

	}
	return render(request,'quotation_form.html',context)






def pdf_view(request,id=id):
    data = Quotation.objects.get(id=id)
    #performa = Performa.objects.get(id=id)
    return render(request,'pdf_generate.html',{"data":data})

def pdf_view_performa(request,id=''):
	data = Performa.objects.get(id=id)
	amount1 = data.quantity * data.per_item_price
	amount = amount1
	amount2 = 0
	amount3 = 0
	amount4 = 0
	amount5 = 0
	if data.quantity2:
		amount2 = int(data.quantity2) * int(data.per_item_price2)
		amount += amount2
	if data.quantity3:
		amount3 = int(data.quantity3) * int(data.per_item_price3)
		amount += amount3
	if data.quantity4:
		amount4 = int(data.quantity4) * int(data.per_item_price4)
		amount += amount4
	if data.quantity5:
		amount5 = int(data.quantity5) * int(data.per_item_price5)
		amount += amount5
	amount = amount + int(data.freight)
	context = {
		"data":data,
		"amount1":amount1,
		"amount2":amount2,
		"amount3":amount3,
		"amount4":amount4,
		"amount5":amount5,
		"amount":amount
	}
	return render(request,'pdf_performa.html',context)


def product_brief(request):
    form = ProductBriefForm()
    if request.method == "POST":
        form = ProductBriefForm(request.POST)
        if form.is_valid():
            
            obj = form.save()
            obj.user = request.user
            
            obj.save()
            return redirect('/product/brief')
    else:
        form = ProductBriefForm()
    return render(request,'new_product_brief.html',{"form":form})

def sales_pdf(request, id=''):
	if id:
		data = Order.objects.get(order_id=id)

	else:
		data = 1
	return render(request, 'sales_order_invoice.html',{"data":data})

def order_information(request,id):
	orders = Order.objects.get(order_id=id)
	return render(request,'pro-list.html',{"orders":orders})

def sample_information(request,id):
	orders = Sample.objects.get(id=id)
	return render(request,'sample_detail.html',{"orders":orders})

def quotation_information(request,id):
	quotation = Quotation.objects.get(id=id)
	return render(request,'qotation_detail.html',{"quotation":quotation})

def performa_information(request,id):
	performa = Performa.objects.get(id=id)
	return render(request,'performa_detail.html',{"performa":performa})


def order_confirmation_information(request,id):
	order = Order.objects.get(order_id=id)
	return render(request,'order_admin_detail.html',{"order":order})

def sample_admin_information(request,id):
	orders = Sample.objects.get(id=id)
	return render(request,'sample_admin_detail.html',{"orders":orders})

def performa_admin_information(request,id):
	performa = Performa.objects.get(id=id)
	return render(request,'performa_admin_detail.html',{"performa":performa})

def quotation_admin_information(request,id):
	quotation = Quotation.objects.get(id=id)
	return render(request,'qotation_admin_detail.html',{"quotation":quotation})

def dispatch_order_information(request,id):
	order = Order.objects.get(order_id=id)
	return render(request, 'dispatch_order_detail.html', {"orders":order})

def lead_information(request,id):
	lead = Lead.objects.get(lead_id=id)
	return render(request,'lead_information.html',{"lead":lead})

def edit_lead(request,id):
	instance = get_object_or_404(Lead, lead_id=id)
	if request.method=="POST":
		form = LeadUpdateForm(request.POST,instance=instance)
		if form.is_valid():
			form.save()
			return redirect('/customer/list')
	else:
		form = LeadUpdateForm(instance=instance)
	return render(request,'edit_lead.html',{"form":form})

def mail_set(request):
    return render(request,'mail-settings.html')