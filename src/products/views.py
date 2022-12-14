from django.shortcuts import render

from .forms import ProductForm

from .models import Product

def product_create_view(request):
	#print(request.GET)
	#print(request.POST)
	if request.method == "POST":
		my_new_title = request.POST.get('title')
		print(my_new_title)
	context = {	}
	return render(request, "products/product_create.html", context)

#def product_create_view(request):
#	form = ProductForm(request.POST or None)
#	if form.is_valid():
#		form.save()
#		form = ProductForm()
#
#	context = {
#			'form': form
#	}
#	return render(request, "products/product_create.html", context)

# Create your views here.
def product_detail_view(request):
	obj = Product.objects.get(id=1)
	#context = {
	#	'title': obj.title,
	#	'description': obj.description,
	#	'price': obj.price
	#}
	context = {
			'object': obj
	}
	return render(request, "products/product_detail.html", context)