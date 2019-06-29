from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import QueryURL,AnswerURL
from skroc_url.forms import InputURLForm,OutputURLForm


def home_view(request,*args,**kwargs):
	#return HttpResponse("<h1>Hello World</h1>")
	context ={"title" : "ZADANIE Rekrutacyjne:"}
	return render(request,"skroc_url/home.html",context)