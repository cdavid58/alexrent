from django.shortcuts import render

def Index(request):
	return render(request,'index.html')

def List_Property(request):
	return render(request,'property/list_property.html')

def Property_Detail(request):
	return render(request,'property/property_details.html')

def About(request):
	return render(request,'about.html')

def Contact(request):
	return render(request,'contact.html')
