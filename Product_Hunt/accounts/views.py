from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth
from products.models import Product

def signup(request):
	if(request.method == 'POST'):
		if(request.POST['password1'] == request.POST['password2']):
			try:
				User.objects.get(username = request.POST['username'])
				return render(request, 'accounts/signup.html', {'error': 'Username is Already Taken!'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
				auth.login(request, user)
				return redirect('home')

		else:
			return render(request, 'accounts/signup.html', {'error':'Password doesn\'t Matched!'})
	else:
		return render(request, 'accounts/signup.html')


def login(request):
	if(request.method == 'POST'):
		user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
		if(user is not None):
			current_user = request.user
			current_user_id = current_user.id
			auth.login(request, user)
			return redirect('home')
		else:
			return render(request, 'accounts/login.html', {'error': 'Username or Password is Invalid!'})
	else:
		logout(request)
		return render(request, 'accounts/login.html')


def login_page(request, user_id):
	user_id = user_id.id
	detail = User.objects.get(pk = user_id)
	data = detail.products.all()
	return render(request, 'accounts/login_page.html', {'detail':data})


def logout(request):
	if(request.method == 'POST'):
		auth.logout(request)
		return redirect('home')


def PD(request):
	return HttpResponse("Hell")