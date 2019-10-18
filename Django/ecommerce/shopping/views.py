from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Product,BuyProduct
from django.views.generic import ListView, DetailView

class ProductListView(ListView):
    queryset = Product.objects.filter(no_of_products__gte=1)
    context_object_name = 'products'
    template_name = 'home.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products.html'

def BuyMenu(request, pk):
	product = Product.objects.get(pk = pk)
	if request.method == 'POST':
		buyer = request.POST['email']
		count = request.POST['count']

		if count=='' or buyer=='':
			return HttpResponse('<h1>emial or count cannot be empty</h1>')

		try:
			user = User.objects.get(email = buyer)
		except User.DoesNotExist:
			return HttpResponse('<h1>User Does not exist</h1>')
		else:
			user = User.objects.get(email = buyer)

		totalamount = (product.cost * int(count))
		buyp = BuyProduct.objects.filter(email=buyer, product_name= product.product_name)

		if int(count)<=0:
			return HttpResponse('<h1>Please enter correct count</h1>')
		elif product.no_of_products < int(count):
			return HttpResponse('<h1>Not Enough Product</h1>')
		elif user.account_balance < totalamount:
			return HttpResponse('<h1>Not Enough Balance</h1>')
		elif buyp:
			buyp[0].items += int(count)
			buyp[0].save()
			user.account_balance = user.account_balance - totalamount
			product.no_of_products = product.no_of_products - int(count)
			user.save()
			product.save()
			return redirect("ProductListView")
		else:
			buyproduct = BuyProduct.objects.create(email = user.email, product_name = product.product_name, cost = product.cost, items = int(count))
			user.account_balance = user.account_balance - totalamount
			product.no_of_products = product.no_of_products - int(count)
			user.save()
			product.save()
			return redirect("ProductListView")
			
	return render(request, 'buy.html', {'product': product})

