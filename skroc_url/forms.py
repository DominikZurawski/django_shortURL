from django import forms 
from .models import QueryURL,AnswerURL

class InputURLForm(forms.ModelForm):
	class Meta:
		model = QueryURL
		fields = [
			'queryURL'			
			]

class OutputURLForm(forms.Form):
	class Meta:
		model = AnswerURL
		fields = [
			'short_URL',
			'URL'
		]
		
	
