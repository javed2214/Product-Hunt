from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . models import Product
from django.utils import timezone

def home(request):
	products = Product.objects.all()
	user = request.user
	if(str(user) == "AnonymousUser"):
		user = ""
	context = {'products':products, 'user':user}
	return render(request, 'products/home.html', context)


@login_required
def create(request):
	if(request.method == 'POST'):
		if(request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']):
			prod = Product()
			prod.title = request.POST['title']
			prod.body = request.POST['body']
			if(request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://')):
				prod.url = request.POST['url']
			else:
				prod.url = 'http://' + request.POST['url']
			prod.icon = request.FILES['icon']
			prod.image = request.FILES['image']
			prod.pub_date = timezone.datetime.now()
			prod.hunter = request.user
			prod.save()
			return redirect('/products/' + str(prod.id))
		else:
			return render(request, 'products/create.html', {'error': 'Please Fill all the Fields!'})
	else:
		return render(request, 'products/create.html')

@login_required
def detail(request, product_id):
	product = get_object_or_404(Product, pk = product_id)
	us = request.user
	return render(request, 'products/detail.html', {'product': product, 'us':us})

@login_required
def upvote(request, product_id):
	if(request.method == 'POST'):
		product = get_object_or_404(Product, pk = product_id)
		x = (product.likes)
		li = list(x.split(' '))
		flag = 0
		print(li)
		for c in li:
			if(c == str(request.user)):
				flag = 1 
				product.total_votes -= 1
				li.remove(str(request.user))
				product.likes = res = str(" ".join(map(str, li))) 
				break;

		if(flag != 1):
			product.likes = product.likes + " "
			product.likes = product.likes + str(request.user)
			product.total_votes += 1

		product.save()
		return redirect('/products/' + str(product.id))


def myproducts(request):
	user = request.user
	pm = Product.objects.all()
	context = {'user':user, 'pm':pm}
	return render(request, 'products/myproducts.html', context)