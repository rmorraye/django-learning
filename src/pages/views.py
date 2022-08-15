from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	#return HttpResponse("<h1>Hello World</h1>") # string of HTML code
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	#return HttpResponse("<h1>My contact</h1>")
	my_context = {
		"my_text": "This is about my USPnumber",
		"my_number": 8124292,
		"phone_number": "(16) 99212-9337",
		"my_list": [21,33,"Abc",42,90],
		"my_html": "<h1>Hello, HTML?!</h1>"
	}	
	return render(request, "contact.html", my_context)