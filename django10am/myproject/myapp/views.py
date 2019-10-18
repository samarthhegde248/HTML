from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register,Custom_User
from .forms import Register_ModelForm,Register_Form
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from django.core.mail import send_mail
from myproject import settings

from django.contrib import messages
# from django.contrib.auth.hashers import set_password

# Create your views here.
def hello(request):
	return HttpResponse("<h1>Hello World!</h1>")


def sample_html(request):
	return render(request,'sample.html')


# ORM -- Object Relational Mappers
# create() -- 
# get()
# filter()
# all()
# update()

# model_name.objects.functon-name

def data_all(request):
	data = Register.objects.all()
	return render(request,'data.html',{'details':data})


def single_data(request,pk):
	data = Register.objects.get(pk=pk)
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']
		mobile=request.POST['mobile']
		data.name=name
		data.email=email
		data.mobile=mobile
		data.save()
		return redirect("data")
	return render(request,'update_form.html',{'details':data})


def delete_user(request,pk):
	data = Register.objects.get(pk=pk)
	data.delete()
	return redirect("data")

# ModelForms -- forms which will be autogeenrated by using model name..
# Forms
# HtmlForms

def register_modelform(request):
	form = Register_ModelForm()
	print(request)
	if request.method=="POST":
		form = Register_ModelForm(request.POST)
		if form.is_valid():
			print(form)
			form.save()
			# return HttpResponse('Data Saved Successfully')
			return redirect('data')
	else:
		form = Register_ModelForm()
	return render(request,'model_form.html',{'form':form})

def register_form(request):
	form=Register_Form()
	if request.method=="POST":
		name = request.POST['name']
		email = request.POST['email']
		mobile = request.POST['mobile']
		Register.objects.create(name=name,email=email,mobile=mobile)
		return HttpResponse("Data Saved Successfully!")
	return render(request,"form.html",{'form':form})

def html_form(request):
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']
		mobile=request.POST['mobile']
		Register.objects.create(name=name,email=email,mobile=mobile)
		return redirect('data')
	return render(request,'html_form.html')

# class based views

# Create View -- 
# Update View -- 
# ListView -- 
# DetailView--
# Deleteview--


class Register_create(CreateView):
	model=Register
	fields="__all__"
	success_url = reverse_lazy('data')
	# template_name = "register_cls_form.html"

class Register_list(ListView):
	model=Register


class Register_detail(DetailView):
	model=Register

class Register_update(UpdateView):
	model=Register
	fields = "__all__"
	success_url = reverse_lazy('data')


class Register_delete(DeleteView):
	model=Register
	success_url = reverse_lazy('data')


# Authentication Management:-


def login_user(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password)
		if user:
			login(request,user)
			messages.success(request,user.username+" Logged in Successfully")
			return redirect('data')
		else:
			messages.warning(request,"Please Check the Credetials")
			return redirect('login')
	return render(request,'myapp/login.html')

def logout_user(request):
	logout(request)
	return redirect('login')


def custom_user_registration(request):
	if request.method=="POST":
		username=request.POST['name']
		email=request.POST['email']
		mobile=request.POST['mobile']
		address=request.POST['address']
		aadhar=request.POST['aadhar']
		password= request.POST['password']
		user = User.objects.create(username=username,email=email)
		Custom_User.objects.create(user=user,mobile=mobile,address=address,aadhar_no=aadhar)
		user.set_password(password)
		user.save()
		subject="Registration Confirmation"
		content = "Thanks for Registering in our website!"
		to = [email]
		from_user = settings.EMAIL_HOST_USER
		# send_mail(subject,content,from_user,to)
		messages.success(request,'Registration is successful!')
		return redirect('data')
	return render(request,'custom_user_registration.html')

def edit_profile(request):
	print(request.user)
	details = User.objects.get(username=request.user.username)
	custom_data = Custom_User.objects.get(user=request.user)
	if request.method == "POST":
		if request.POST['username'] or request.POST['email']:
			details.username=request.POST['username']
			details.email= request.POST['email']
			if request.POST['password']:
				details.set_password(request.POST['password'])
			details.save()

		if request.POST['mobile'] or request.POST['address'] or request.POST['aadhar_no']:
			custom_data.mobile = request.POST['mobile']
			custom_data.address = request.POST['address']
			custom_data.aadhar_no = request.POST['aadhar_no']
			custom_data.save()
		return HttpResponse("Profile Updated Successfully!") 
	return render(request,'edit_profile.html',{'details':details,'custom_data':custom_data})
