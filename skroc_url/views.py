from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import QueryURL,AnswerURL
from skroc_url.forms import InputURLForm,OutputURLForm


def home_view(request,*args,**kwargs):
	#return HttpResponse("<h1>Hello World</h1>")
	context ={"title" : "ZADANIE Rekrutacyjne:"}
	return render(request,"skroc_url/home.html",context)

def index(request):
	return render(request, 'skroc_url/index.html', context)

def inputURL_view(request):   
	form = InputURLForm(request.POST or None)
	if form.is_valid():
		OutputURLForm.shortURL = form.save(commit=False)
		link = form.save(commit=False)
		form.save()
		form = InputURLForm
		return render(request, 'skroc_url/outputURL.html', {"link": OutputURLForm.shortURL,"info" : "Twój link! "})
	else: 
		form = InputURLForm()		
			
	context = {"description" : "Wklej adres URL:",
			   "form" : form,
			   }
	return render(request, "skroc_url/inputURL.html", context)	